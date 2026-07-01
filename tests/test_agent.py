"""Tests for agent.py — teaching agent with mocked Anthropic API."""

from datetime import datetime
from unittest.mock import MagicMock

import anthropic
import httpx
import networkx as nx
import pytest

import agent
from agent import build_system_prompt, build_messages, ask, resolve_model


def _make_mock_client(response_text="Here is my explanation."):
    """Create a mock Anthropic client that returns a canned response."""
    client = MagicMock()
    mock_response = MagicMock()
    text_block = MagicMock()
    text_block.type = "text"
    text_block.text = response_text
    mock_response.content = [text_block]
    mock_response.usage.input_tokens = 100
    mock_response.usage.output_tokens = 50
    client.messages.create.return_value = mock_response
    return client


def _make_test_graph():
    """Create a small graph for agent tests."""
    g = nx.DiGraph()
    g.add_node("Class", content="Classes are blueprints for [[Object]]s.")
    g.add_node("Object", content="Everything in Python is an [[Object]].")
    g.add_edge("Class", "Object")
    g.add_edge("Object", "Class")
    return g


# ── Group F: build_system_prompt ────────────────────────────────────────


class TestBuildSystemPrompt:
    def test_contains_topic_content(self):
        context = {
            "topic": "Class",
            "content": "Classes are blueprints.",
            "neighbors": {},
        }
        prompt = build_system_prompt(context)
        assert "Classes are blueprints." in prompt

    def test_contains_neighbor_content(self):
        context = {
            "topic": "Class",
            "content": "Classes are blueprints.",
            "neighbors": {"Object": "Everything is an Object."},
        }
        prompt = build_system_prompt(context)
        assert "Everything is an Object." in prompt
        assert "Object" in prompt

    def test_contains_tutor_methodology(self):
        context = {
            "topic": "Class",
            "content": "Classes are blueprints.",
            "neighbors": {},
        }
        prompt = build_system_prompt(context)
        assert "Socratic" in prompt
        assert "Teaching Methodology" in prompt

    def test_no_topic_found(self):
        context = {"topic": "xyzzy", "content": None, "neighbors": {}}
        prompt = build_system_prompt(context)
        assert isinstance(prompt, str)
        assert "Socratic" in prompt  # tutor prompt still present

    def test_no_topic_fallback_is_language_agnostic(self):
        context = {"topic": "xyzzy", "content": None, "neighbors": {}}
        prompt = build_system_prompt(context)
        assert "Python" not in prompt


# ── Group G: build_messages ─────────────────────────────────────────────


class TestBuildMessages:
    def test_first_message_no_history(self):
        msgs = build_messages([], "What is a class?")
        assert msgs == [{"role": "user", "content": "What is a class?"}]

    def test_appends_to_history(self):
        history = [
            {"role": "user", "content": "Hi"},
            {"role": "assistant", "content": "Hello!"},
        ]
        msgs = build_messages(history, "What is a class?")
        assert len(msgs) == 3
        assert msgs[-1] == {"role": "user", "content": "What is a class?"}

    def test_preserves_history_order(self):
        history = [
            {"role": "user", "content": "First"},
            {"role": "assistant", "content": "Response"},
        ]
        msgs = build_messages(history, "Second")
        assert msgs[0]["content"] == "First"
        assert msgs[1]["content"] == "Response"
        assert msgs[2]["content"] == "Second"


# ── Group H: ask (mocked API) ──────────────────────────────────────────


class TestAsk:
    def test_calls_api_with_correct_model(self, monkeypatch):
        graph = _make_test_graph()
        client = _make_mock_client()
        ask(graph, "What is a class?", [], client=client)
        call_kwargs = client.messages.create.call_args
        assert "claude" in call_kwargs.kwargs.get("model", "").lower() or \
               "claude" in (call_kwargs.args[0] if call_kwargs.args else "").lower()

    def test_returns_response_text(self):
        graph = _make_test_graph()
        client = _make_mock_client("Classes are blueprints for objects.")
        response, _, _ = ask(graph, "What is a class?", [], client=client)
        assert response == "Classes are blueprints for objects."

    def test_updates_conversation_history(self):
        graph = _make_test_graph()
        client = _make_mock_client("Here is my answer.")
        _, history, _ = ask(graph, "What is a class?", [], client=client)
        assert len(history) == 2
        assert history[0] == {"role": "user", "content": "What is a class?"}
        assert history[1] == {"role": "assistant", "content": "Here is my answer."}

    def test_returns_usage(self):
        graph = _make_test_graph()
        client = _make_mock_client()
        _, _, usage = ask(graph, "What is a class?", [], client=client)
        assert usage["input_tokens"] == 100
        assert usage["output_tokens"] == 50
        assert "retrieval" in usage
        assert usage["retrieval"]["topic"] is not None
        assert isinstance(usage["retrieval"]["score"], float)
        assert isinstance(usage["retrieval"]["neighbors"], int)

    def test_handles_unknown_topic(self):
        graph = _make_test_graph()
        client = _make_mock_client("I'm not sure about that topic.")
        response, history, _ = ask(graph, "xyzzy plugh", [], client=client)
        assert response == "I'm not sure about that topic."
        # API was still called
        client.messages.create.assert_called_once()


# ── Group I: TF-IDF retrieval integration ──────────────────────────────


class TestTfidfRetrieval:
    def test_natural_language_query_retrieves_relevant_note(self, tfidf_graph):
        """A question phrased nothing like a note title should still ground
        the prompt in the right note via TF-IDF content search."""
        client = _make_mock_client()
        # This query doesn't match any title, but its vocabulary overlaps
        # heavily with the Decorator note body
        response, _, _ = ask(
            tfidf_graph,
            "how do I wrap a function to modify its behavior",
            [],
            client=client,
        )
        system_prompt = client.messages.create.call_args.kwargs["system"]
        assert "decorator" in system_prompt.lower()


# ── Group J: model resolution ───────────────────────────────────────────


def _model_entry(model_id, created_at):
    """Fake Models API entry with id and created_at."""
    entry = MagicMock()
    entry.id = model_id
    entry.created_at = created_at
    return entry


def _not_found_error():
    req = httpx.Request("GET", "https://api.anthropic.com/v1/models/x")
    resp = httpx.Response(404, request=req)
    return anthropic.NotFoundError("model not found", response=resp, body=None)


def _server_error():
    req = httpx.Request("GET", "https://api.anthropic.com/v1/models/x")
    resp = httpx.Response(529, request=req)
    return anthropic.APIStatusError("overloaded", response=resp, body=None)


class TestResolveModel:
    def test_default_pin_is_sonnet_5(self):
        assert getattr(agent, "DEFAULT_MODEL", None) == "claude-sonnet-5"

    def test_returns_configured_when_valid(self):
        client = MagicMock()
        client.models.retrieve.return_value = MagicMock()
        assert resolve_model(client, "claude-sonnet-5") == "claude-sonnet-5"
        client.models.list.assert_not_called()

    def test_defaults_to_module_model(self, monkeypatch):
        monkeypatch.setattr(agent, "MODEL", "claude-test-pin")
        client = MagicMock()
        client.models.retrieve.return_value = MagicMock()
        assert resolve_model(client) == "claude-test-pin"
        client.models.retrieve.assert_called_once_with("claude-test-pin")

    def test_falls_back_to_newest_sonnet_on_404(self):
        client = MagicMock()
        client.models.retrieve.side_effect = _not_found_error()
        # Opus is newest overall — must NOT be picked; newest *Sonnet* wins.
        client.models.list.return_value = [
            _model_entry("claude-opus-9", datetime(2027, 5, 1)),
            _model_entry("claude-sonnet-4-6", datetime(2025, 11, 24)),
            _model_entry("claude-sonnet-5", datetime(2026, 6, 20)),
            _model_entry("claude-haiku-4-5-20251001", datetime(2025, 10, 1)),
        ]
        assert resolve_model(client, "claude-sonnet-4-0") == "claude-sonnet-5"

    def test_raises_when_no_sonnet_available(self):
        client = MagicMock()
        client.models.retrieve.side_effect = _not_found_error()
        client.models.list.return_value = [
            _model_entry("claude-opus-9", datetime(2027, 5, 1)),
        ]
        with pytest.raises(RuntimeError):
            resolve_model(client, "claude-sonnet-4-0")

    def test_fail_open_on_connection_error(self):
        client = MagicMock()
        client.models.retrieve.side_effect = anthropic.APIConnectionError(
            request=httpx.Request("GET", "https://api.anthropic.com/v1/models/x")
        )
        assert resolve_model(client, "claude-sonnet-5") == "claude-sonnet-5"

    def test_fail_open_on_server_error(self):
        client = MagicMock()
        client.models.retrieve.side_effect = _server_error()
        assert resolve_model(client, "claude-sonnet-5") == "claude-sonnet-5"


class TestAskModelParam:
    def test_uses_explicit_model(self):
        graph = _make_test_graph()
        client = _make_mock_client()
        ask(graph, "What is a class?", [], client=client, model="claude-explicit-x")
        assert client.messages.create.call_args.kwargs["model"] == "claude-explicit-x"

    def test_defaults_to_module_model_when_not_passed(self, monkeypatch):
        monkeypatch.setattr(agent, "MODEL", "claude-default-y")
        graph = _make_test_graph()
        client = _make_mock_client()
        ask(graph, "What is a class?", [], client=client)
        assert client.messages.create.call_args.kwargs["model"] == "claude-default-y"


# ── Group K: thinking-block handling (regression) ──────────────────────


class TestThinkingBlocks:
    def test_ask_skips_thinking_blocks(self):
        """Sonnet 5 responses can lead with a ThinkingBlock; ask() must return
        the first *text* block, not blow up on content[0].text (prod 500, 2026-07-01)."""
        graph = _make_test_graph()
        client = MagicMock()
        thinking_block = MagicMock(spec=["type", "thinking"])
        thinking_block.type = "thinking"
        text_block = MagicMock()
        text_block.type = "text"
        text_block.text = "Here is the actual answer."
        mock_response = MagicMock()
        mock_response.content = [thinking_block, text_block]
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50
        client.messages.create.return_value = mock_response
        response, history, _ = ask(graph, "What is a class?", [], client=client)
        assert response == "Here is the actual answer."
        assert history[-1] == {"role": "assistant", "content": "Here is the actual answer."}
