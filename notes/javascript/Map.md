Created: 2024-08-24 09:30

Used with [[Array]]s, passes each element of the [[Array]], one-by-one, to the [[Callback function]] that's its argument. Uses the [[Return value]] of each [[Callback function]] [[Function call]] to fill up the new [[Array]] that it returns:

```js
const numbers = [1, 4, 9];
const roots = numbers.map((num) => Math.sqrt(num));

// roots is now     [1, 2, 3]
// numbers is still [1, 4, 9]
```
## References
1. [ Intro to JS > Loops & Iterations ](https://launchschool.com/books/javascript/read/loops_iterating#forloops)
2. [ MDN Docs ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)