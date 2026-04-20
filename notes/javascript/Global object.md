Created: 2024-11-16 09:01

The global object is the implicit [[Execution context]] for code running in JavaScript at the **top level** of the program (except for `.js` files executed by Node). What is is exactly, and how it works **depends on how the code is run**: 
* If run in a browser it is `window`.
* If run in Node's REPL it is `global`.

When a `.js` file is executed by Node, the program is **wrapped in a function**:
```js
(function (exports, require, module, __filename, __dirname) {
   // your code is here
});
```
and the [[Execution context]] at the **top level** is an empty [[Object]]. We still can access the **global object** through `global`. Calling **module scope** the [[Lexical scoping]] environment of a program executed in a `.js` file by Node, we can analyze it as follows:
```js
var foo = 'foo';
// with `var`, the variable is in the module scope
// and not added to the global object

bar = 'bar';
// without `var` declaration, the variable is in the global scope
// and added to the global object

let qux = 'qux';
// with `let`, the variable is in the module scope
// and is not added to the global object

console.log(global.foo);    // => undefined
console.log(global.bar);    // => bar
console.log(global.qux);    // => undefined
console.log(qux);           // => qux
```
Bear in mind that we are **not** attaching them to the [[Execution context]]:
```js
var foo = 'foo';
bar = 'bar';
let qux = 'qux';

console.log(this.foo);    // => undefined
console.log(this.bar);    // => undefined
console.log(this.qux);    // => undefined
console.log(this);        // => {}
```

In [[Strict mode]], even though the [[this]] variable returns what you would expect normally, it is **not accessible**, i.e. it acts as if the [[Execution context]] is `undefined` (except when running in Node's REPL).

---
Although you **can** `delete` native [[Method]]s from the global object, the same isn't true for [[Variable]]s and [[Function]]s declared at the global scope:
```js
> delete window.isNaN
< true
> window.isNaN
< undefined
> function isNaN() {
      console.log('no, it is not.');
  }
> window.isNaN
< ƒ isNaN() {
      console.log('no, it is not.');
  }
> delete window.isNaN
< false
```
## References
1. [ JS225 > Function Context and Objects > Global Object ](https://launchschool.com/lessons/c9200ad2/assignments/c8e3c9a4)