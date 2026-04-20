Created: 2024-08-19 19:18

Basic syntax:
```js
for (initialization; condition; increment) {
  // loop body
}
```
It behaves almost the same as the [[While loop]] arranged like so:
```js
initialization;
while (condition) {
  // loop body
  increment;
}
```
The only difference is the [[Variable scope]] of the [[Variable]] declared in the initialization clause. In the [[While loop]] its scope includes the outer scope whereas in the for [[Statement]] it's only the [[Block]] which is its body.

You can skip any of the three components of the `for` statement (`initialExpression`, `condition`, and `incrementExpression`). For example:
```js
// put initialization outside of the loop

let index = 0;
for (; index < 10; index += 1) {
  console.log(index);
}

// manually check condition and break out of the loop
// If you omit the condition component in the "for", JavaScript assumes true

for (let index = 0; ; index += 1) {
  if (index >= 10) {
    break;
  }

  console.log(index);
}

// manually increment the iterator

for (let index = 0; index < 10; ) {
  console.log(index);
  index += 1;
}
```
## References
1. [ Intro to JS > Loops & Iterations ](https://launchschool.com/books/javascript/read/loops_iterating#forloops)