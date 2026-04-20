Created: 2024-08-19 15:30

These are [[Expression]]s that always has [[Boolean]] as [[Return value]]. They compare two *operands*, to the left and right hand side of themselves. Some common ones are:
* [[Strict equality]]
* [[Strict inequality]]
* [[Loose equality]]
* [[Loose inequality]]
* [[Greater than]]
* [[Less than]]
They often work alongside [[Logical operator]]

They'll obey [[Operator precedence]].

---
[[NaN]] is especially tricky when dealing with comparisons. 

Since we can't use the usual comparison *operators* to compare [[NaN]] with other [[Value]]s, how can we check whether a [[Variable]] holds [[NaN]]? JavaScript provides a solution: the `Number.isNaN` [[Function]] returns `true` if a value is not a number, `false` otherwise:
```js
let foo = NaN;
console.log(Number.isNaN(foo));      // true

console.log(Number.isNaN('hello'));  // return false since `'hello'` is not NaN
```
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)