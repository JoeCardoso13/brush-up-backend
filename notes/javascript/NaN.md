Created: 2024-08-21 19:22

Stands for "Not a Number". It is a [[Number]].

A problematic feature of `NaN` is that comparing it with any [[Value]] evaluates to `false` even if that [[Value]] is `NaN` itself. In other words, `NaN` is not equal to `NaN`!
```js
console.log(10 === NaN);     // false
console.log(10 < NaN);       // false
console.log(10 > NaN);       // false
console.log(NaN === NaN);    // false
```

`NaN` is the only [[Value]] in JavaScript that is **not** equal itself, therefore, we could write a function like this:
```js
function isNotANumber(value) {
  return value !== value;
}
```
That is equivalent to the [[Method]] `Number.isNaN()`.

## References
1. [ Intro to JS > More Stuff ](https://launchschool.com/books/javascript/read/more_stuff)