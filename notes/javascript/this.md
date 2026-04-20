Created: 2024-11-14 11:33

The `this` keyword provides the current [[Execution context]] for code running in JavaScript.

Every time a JavaScript [[Function]] is invoked, it has access to an [[Object]] that is the [[Execution context]] of that [[Function]]. This execution context is accessible through the keyword `this`. To illustrate:
```js
let obj = {
  foo() {
    return this;
  },
};

let context = obj.foo();

console.log(context); // logs the object referenced by obj
```

A JavaScript [[Function]] can be invoked in a variety of ways. What [[Object]] `this` refers to depends on how the function was invoked.

Its most common usage is when defining [[Method]]s. In a [[Method]] invocation/call `this` refers to the [[Object]] caller as the [[Execution context]]:
```js
let counter = {
  count: 0,
  advance: function() {
    this.count += 1;
  },
};

counter;                // { count: 0, advance: [Function] }

counter.advance();
counter;                // { count: 1, advance: [Function] }

counter.advance();
counter.advance();

counter;                // { count: 3, advance: [Function] }
```
[[Object]]'s [[Method]]s are just properties that happen to have a [[Function]] [[Value]]. They can be created anytime, in the [[Object]] definition when you [[Create object]] in its [[Literal form]] or later by assigning a [[Function]] to a new property. 

[[Function]]s initially have no context, they receive one when the program executes them. JavaScript creates a [[Global object]] when it starts running, which serves as the **implicit** [[Execution context]] (except for code run in a `.js` file with Node, where the **implicit** [[Execution context]] is an empty [[Object]] or code running in [[Strict mode]] where even though `this` returns what you would expect if the code was running without [[Strict mode]] at the **top level**, it returns `undefined` when being the **implicit** [[Execution context]] of a [[Function invocation]]).

Be **careful** with the value of **this** in [[Function definition]]s of arguments of build-in higher-order [[Function]]s. If **not** [[Arrow function]] it resolves to the [[Global object]]!
## References
1. [ OO JS book > Objects ](https://launchschool.com/books/oo_javascript/read/types_and_objects)