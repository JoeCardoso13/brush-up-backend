Created: 2024-08-19 10:37

Represents all kinds of numbers: integers, floating-point numbers, and fixed-point (decimal) etc:
```
1, 2, -3, 4.5, -6.77, 234891234 // Examples of numeric literals
```

JavaScript uses [[Implicit type coercion]] for operations between [[Number]]s and [[String]]s.

---
[[NaN]], which stands for 'Not a Number' is a data of [[Type]] number. It has a weird behavior when compared against itself:
```
> NaN === NaN
= false

> NaN !== NaN
= true
```
`Number.isNaN(value)` or `Object.is(value, NaN)` are ways to check if a [[Value]] is [[NaN]].

`Infinity` is a number [[Greater than]] any number.
`-Infinity` is a number [[Less than]] any number.

---
To get digits from a number, you can iterate through powers of `10` in the denominator of an [[Expression]] using division and remainder as follows:
```
> let n = 4321
undefined
> n % 10
1
> Math.floor(n / 10) % 10
2
> Math.floor(n / 100) % 10
3
> Math.floor(n / 1000) % 10
```
## References
1. [ Intro to JS > Basics ](https://launchschool.com/books/javascript/read/basics#datatypes)