"""FastAPI backend for the brush-up multi-language tutor."""

import logging
import os
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

import anthropic
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from agent import ask
from budget import check_budget, record_usage
from graph import TfidfIndex, build_tutors

Tutor = Literal["python", "ruby", "javascript"]

logger = logging.getLogger("brush-up")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

# ── Configuration ──────────────────────────────────────────────────────

NOTES_DIR = Path(__file__).resolve().parent.parent / "notes"

DEFAULT_ALLOWED_ORIGINS = (
    "https://joecardoso.dev",
    "https://www.joecardoso.dev",
    "http://localhost:4321",
)
DEFAULT_ALLOWED_ORIGIN_REGEX = r"^https://[-a-zA-Z0-9]+\.vercel\.app$"


def _parse_allowed_origins() -> list[str]:
    configured = os.environ.get("BRUSH_UP_ALLOWED_ORIGINS")
    if not configured:
        return list(DEFAULT_ALLOWED_ORIGINS)

    return [origin.strip() for origin in configured.split(",") if origin.strip()]


def _parse_allowed_origin_regex() -> str | None:
    return os.environ.get("BRUSH_UP_ALLOWED_ORIGIN_REGEX", DEFAULT_ALLOWED_ORIGIN_REGEX)


ALLOWED_ORIGINS = _parse_allowed_origins()
ALLOWED_ORIGIN_REGEX = _parse_allowed_origin_regex()


# ── App lifecycle ──────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    graphs = build_tutors(NOTES_DIR)
    app.state.tutors = {name: (g, TfidfIndex(g)) for name, g in graphs.items()}
    app.state.client = anthropic.Anthropic(max_retries=3)
    app.state.budgets = {}
    for name, (g, _) in app.state.tutors.items():
        logger.info("Tutor %s loaded: %d topics", name, g.number_of_nodes())
    yield


app = FastAPI(title="brush-up", docs_url=None, redoc_url=None, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_origin_regex=ALLOWED_ORIGIN_REGEX,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# ── Request / response models ──────────────────────────────────────────


class ChatRequest(BaseModel):
    user_id: str = Field(min_length=1, max_length=100)
    tutor: Tutor
    question: str = Field(min_length=1, max_length=2000)
    conversation_history: list[dict] = Field(default_factory=list, max_length=50)


class ChatResponse(BaseModel):
    response: str
    history: list[dict]
    usage: dict


# ── Endpoints ──────────────────────────────────────────────────────────


@app.post("/api/chat")
def chat(req: ChatRequest, request: Request):
    tutors = request.app.state.tutors
    if req.tutor not in tutors:
        return JSONResponse(
            status_code=503,
            content={"error": "tutor_unavailable", "detail": f"Tutor {req.tutor!r} is not loaded."},
        )
    graph, index = tutors[req.tutor]
    client = request.app.state.client
    budgets = request.app.state.budgets

    if not check_budget(budgets, req.user_id):
        logger.info("budget exceeded user=%s", req.user_id[:8])
        return JSONResponse(
            status_code=429,
            content={
                "error": "budget_exceeded",
                "detail": "You've used your token allocation. Thanks for trying brush-up!",
            },
        )

    start = time.monotonic()
    try:
        response_text, updated_history, usage = ask(
            graph, req.question, req.conversation_history, client=client, index=index
        )
    except anthropic.APIStatusError as exc:
        if exc.status_code == 529:
            logger.warning("anthropic overloaded user=%s", req.user_id[:8])
            return JSONResponse(
                status_code=503,
                content={"error": "overloaded", "detail": "The AI service is temporarily busy. Please try again in a moment."},
            )
        logger.error("anthropic error user=%s: %s", req.user_id[:8], exc)
        return JSONResponse(
            status_code=502,
            content={"error": "api_error", "detail": "Something went wrong calling the AI service. Please try again."},
        )
    except anthropic.APIError as exc:
        logger.error("anthropic error user=%s: %s", req.user_id[:8], exc)
        return JSONResponse(
            status_code=502,
            content={"error": "api_error", "detail": "Something went wrong calling the AI service. Please try again."},
        )
    elapsed = time.monotonic() - start

    record_usage(budgets, req.user_id, usage["input_tokens"], usage["output_tokens"])

    retrieval = usage.get("retrieval", {})
    logger.info(
        "chat user=%s q_len=%d tokens=%d+%d %.1fs topic=%r score=%.3f neighbors=%d",
        req.user_id[:8],
        len(req.question),
        usage["input_tokens"],
        usage["output_tokens"],
        elapsed,
        retrieval.get("topic"),
        retrieval.get("score", 0.0),
        retrieval.get("neighbors", 0),
    )

    return ChatResponse(response=response_text, history=updated_history, usage=usage)


@app.get("/api/health")
def health(request: Request):
    tutors = request.app.state.tutors
    return {
        "status": "ok",
        "tutors": {name: g.number_of_nodes() for name, (g, _) in tutors.items()},
    }
