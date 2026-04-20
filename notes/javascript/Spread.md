Created: 2024-08-22 11:52

It's the use of `...` to expand an array to a list of values:
```js
let arr = ['a', 'b', 'c'];
let copyOfArr = [...arr];
copyOfArr; // => [ 'a', 'b', 'c' ];
```
Also works with [[Object]]s:
```js
let foo = { qux: 1, baz: 2 };
let bar = { ...foo };
console.log(bar);         // { qux: 1, baz: 2 }
```
Similar to [[Rest]].
## References
1. [ courses > JS210 > lesson 5 ](https://launchschool.com/lessons/79b41804/assignments/40b5852e)