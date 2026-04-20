Created: 2024-08-19 11:07

Defined by the keywords listed in [2]. They may contain [[Expression]]s but they don't release a [[Return value]] other than [[Undefined]]. I.e. they don't resolve to useful [[Value]]s. This means that you **cannot** use a statement as part of an [[Expression]]:
```
> 5 * let foo
SyntaxError: Unexpected identifier

> console.log(let bar)
SyntaxError: missing ) after argument list
```

If you try to create an [[Expression]] dependent on the statement's [[Return value]] you might get an error:
```js
console.log(let answer = 3 * 5); // SyntaxError: missing ) after argument list
console.log(while (true) {});    // SyntaxError: Unexpected token 'while'
```
Such a thing would **never** happen if you depend on an [[Expression]]'s [[Return value]], in other words, you can rely on these, but not on those.
## References
1. [ Intro to JS > Statements ](https://launchschool.com/books/javascript/read/basics#statements)
2. [MDN list of statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)