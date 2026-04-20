Created: 2024-08-19 18:27

`&&`

Returns the truthy *operand* to the right only when **both** *operands* are evaluated as such according to their [[Truthiness]]. Returns the falsy *operand* otherwise (the one to the left if both are falsy).

Examples:
```js
> true && true
= true

> true && false
= false

> false && true
= false

> false && false
= false

> (4 === 4) && (5 === 5)
= true

> (4 === 4) && (5 === 6)
= false

> (4 === 5) && (5 === 5)
= false

> (4 === 5) && (5 === 6)
= false

> 3 && 'foo'  // last evaluated operand is 'foo'
= 'foo'

> 'foo' && 3  // last evaluated operand is 3
= 3

> 0 && 'foo'  // last evaluated operand is 0
= 0

> 'foo' && 0  // last evaluated operand is 0
= 0
```
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)