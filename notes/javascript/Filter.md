Created: 2024-08-24 09:42

Used with [[Array]]s, passes each element of the [[Array]], one-by-one, to the [[Callback function]] that's its argument. Evaluates the [[Return value]] of each [[Callback function]] [[Function call]] in terms of its [[Truthiness]] and fills up the returned [[Array]] with the original [[Array]] for which evaluation turned out truthy. This returned [[Array]] will be like [[Copying an object]] from the original.

```js
function isBigEnough(value) {
  return value >= 10;
}

const filtered = [12, 5, 8, 130, 44].filter(isBigEnough);
// filtered is [12, 130, 44]
```
## References
1. [ Intro to JS > Loops & Iterations ](https://launchschool.com/books/javascript/read/loops_iterating#forloops)
2. [ MDN Docs ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#iterative_methods)