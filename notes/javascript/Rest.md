Created: 2024-08-27 18:20

It's the use of `...` for collecting multiple items (often used in [[Function call]]s):
```js
let foo = [1, 2, 3, 4];
let [ bar, ...otherStuff ] = foo;
console.log(bar);        // 1
console.log(otherStuff); // [2, 3, 4]
```
Also works with [[Object]]s:
```js
let foo = {bar: 1, qux: 2, baz: 3, xyz: 4};
let { bar, baz, ...otherStuff } = foo;
console.log(bar);        // 1
console.log(baz);        // 3
console.log(otherStuff); // {qux: 2, xyz: 4}
```
## References
1. [ courses > JS210 > lesson 6 ](https://launchschool.com/gists/2edcf7d7)