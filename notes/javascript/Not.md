Created: 2024-08-19 18:25

`!`

Only takes one *operand*. It evaluates the [[Truthiness]] of its operand and returns the [[Boolean]] equivalent to the opposite, i.e. `true` if falsy and `false` if truthy.

Examples:
```js
> !true
= false

> !false
= true

> !(4 === 4)
= false

> !(4 !== 4)
= true
```

It's common to concatenate 2 of them in order to extract the [[Boolean]] equivalent of an [[Expression]].
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)