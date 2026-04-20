Created: 2024-08-19 12:48

In order to be used (have a [[Function call]]), [[Function]]s must first be defined. Example:
```js
function funcName(parameter) {
  func_body;
}
```

The name(s) between parenthesis in a function definition are the **parameters**. They become [[Local variable]]s once the [[Function call]] is made. They'll reference the argument(s) given in the [[Function call]].

You can make a [[Function]] definition parameter quantity agnostic by 2 ways:
* The **traditional** way, using built-in [[Array]]-like `arguments` from JS.
* Using [[Spread]] syntax as **rest parameters**.

Parameters can be given a default [[Value]] through the following syntax:
```js
function say(text = "hello") {
  console.log(text + "!");
}

say("Howdy"); // => Howdy!
say();        // => hello!
```

[[Function]]s can be defined through 3 different ways:
* [[Function declaration]]
* [[Function expression]]
* [[Arrow function]]
They all (even the [[Function declaration]]) generate a [[Variable]] with their own name.
## References
1. [ Intro to JS > Functions & Scope ](https://launchschool.com/books/javascript/read/functions#functionsscope)