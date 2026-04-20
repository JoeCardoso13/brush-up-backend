Created: 2024-08-19 18:35

JavaScript coerces any [[Expression]] to its [[Boolean]] equivalent when in a conditional context (e.g. part of an [[if Statement]]). [[Expression]]s that evaluate as a [[Boolean]] `true` are said to the **truthy**, the others evaluate as a [[Boolean]] `false` and are said to be **falsy**.

JavaScript considers all [[Value]]s **truthy** with the exception of the following **falsy** [[Value]]s:
* `false`
* [[Number]] `0` (in all its variants: `-0`, `0n`)
* Empty [[String]] `''`
* [[Undefined]]
* [[Null]]
* [[NaN]]
Any [[Value]] not in the list above is truthy, including:
```js
if ([])           // truthy
if ({})           // truthy
if ('0')           // truthy
if ('false')           // truthy
if (-1)           // truthy
```

We can user double [[Not]] or `Boolean(value)` to extract the [[Boolean]] equivalent of the truthiness of a [[Value]].
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)