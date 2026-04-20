Created: 2024-08-19 19:31

Used with [[Array]]s, passes each element of the [[Array]], one-by-one, to the [[Callback function]] that's its argument. Its [[Return value]] is [[Undefined]].

Example:
```js
let names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor'];

names.forEach(function(name) {
  console.log(name);
});
```
which can be made more compact with the use of [[Arrow function]]:
```js
let names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor'];

names.forEach(name => console.log(name));
```

Can't use `break` or `continue` or `return`!

A forEach loop can **never** end before it iterates through the whole list. Actually most [[Array]] processing [[Method]]s in JS are like this.
## References
1. [ Intro to JS > Loops & Iterations ](https://launchschool.com/books/javascript/read/loops_iterating#forloops)