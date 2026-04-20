Created: 2024-08-19 18:05

`===`

Also known as 'identity operator', returns `true` if both *operands* have the same [[Type]] **and** [[Value]], `false` otherwise. They **never** perform [[Implicit type coercion]].

[[Array]]s and [[Object]]s don't work well with equality:
```
> [1, 2, 3] === [1, 2, 3]
= false
```
They don't compare [[Value]]s inside the container [[Object]] at all, but simply the container itself:
```
> let a = [1, 2, 3]
> let b = a
> a === b
> = true
```
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)