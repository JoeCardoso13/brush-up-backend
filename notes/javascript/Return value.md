Created: 2024-08-19 11:01

Is the 'result', or 'outcome', of any [[Expression]], a [[Value]] that can be captured and reused throughout the code.

It is an important part of the distinction between [[Expression]] and [[Statement]]:
```js
let foo = false;  // returns undefined

let foo;
foo = false      // returns false
```
The reason why the last line returns `false` is due to it being an [[Expression]].
## References
1. [ Intro to JS > Expressions ](https://launchschool.com/books/javascript/read/basics#expressionsandreturnvalues)