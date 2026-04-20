Created: 2024-08-19 18:20

Commonly used to combine [[Comparison]] [[Expression]]s in an [[if Statement]].
* [[Not]]
* [[And]]
* [[Or]]
They use short-circuit evaluation. This means that, when JS is compiling them, it stops and returns the current [[Value]] whenever the result is guaranteed.

It is common to use the short-circuit evaluation behavior to make a compact guard clause against falsy values, like so:
```js
let myVariable = myVariable || desiredDefaultValue;
```
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)