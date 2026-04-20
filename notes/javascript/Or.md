Created: 2024-08-19 18:29

`||`

Returns whichever truthy *operand* it finds, evaluated as such according to its [[Truthiness]]. Returns the falsy *operand* to the right otherwise.

Examples:
```js
> true || true
= true

> true || false
= true

> false || true
= true

> false || false
= false

> (4 === 4) || (5 === 5)
= true

> (4 === 4) || (5 === 6)
= true

> (4 === 5) || (5 === 5)
= true

> (4 === 5) || (5 === 6)
= false

> 3 || 'foo'  // last evaluated operand is 3
= 3

> 'foo' || 3  // last evaluated operand is 'foo'
= 'foo'

> 0 || 'foo'  // last evaluated operand is 'foo'
= 'foo'

> 'foo' || 0  // last evaluated operand is 'foo'
= 'foo'

> '' || 0     // last evaluated operand is 0
= 0
```

The **nullish coalescing operator** - `??` - is similar to **or** but considers falsy only [[Null]] or [[Undefined]], i.e. it doesn't use JavaScript standard, built-in [[Truthiness]] evaluation.

Examples:
```js
> null ?? "over here!"
= 'over here!'

> undefined ?? "pick me!"
= 'pick me!'

> false ?? "not me"
= false

> 0 ?? "not me either"
= 0

> null ?? "over here!"    // does not short-circuit
= 'over here!

> undefined ?? "pick me!" // does not short-circuit
= 'pick me!'

> false ?? "not me"       // short-circuits
= false

> 0 ?? "not me either"    // short-circuits
= 0
```
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)