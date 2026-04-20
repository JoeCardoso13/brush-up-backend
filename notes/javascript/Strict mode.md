Created: 2024-11-16 10:08

In strict mode, the [[Global object]] is **not** used as the **implicit** [[Execution context]]. Instead, the implicit context is `undefined`. Running on a browser:
```js
"use strict";

oneFoo = 1;        // Uncaught ReferenceError: oneFoo is not defined
oneFoo;

function foo() {
  console.log(this);
}

foo();                // "this here is: undefined"
```
Among other things, this guards against misspellings adding new properties to the [[Global object]].

You can't really check it by logging [[this]] at the **top level**:
```js
"use strict"

console.log(this === window) // true

function foo() {
  console.log(this === window); // false
}

foo();
```

Doesn't work in Node's REPL.
## References
1. [ JS225 > Function Context and Objects > Global Object ](https://launchschool.com/lessons/c9200ad2/assignments/c8e3c9a4)