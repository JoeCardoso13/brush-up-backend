Created: 2024-08-19 14:31

Similar to [[Function call]] in what they do, but the way you call them is completely different:
```js
'xyzzy'.toUpperCase()
```
Here `String.prototype.toUpperCase()` is being called by string `xyzzy`, which acts as if it was a parameter in a [[Function call]].
## References
1. [ Intro to JS > Functions vs Methods ](https://launchschool.com/books/javascript/read/functions#functionsvsmethods)