Created: 2024-08-19 15:25

The `if` [[Statement]] has 2 forms:
```js
if (conditional_1) {
  // body
} else if (conditional_2) {
  // body
} else {
  // body
}
```
And the single line:
```js
if (conditional) expression;
```

The conditional will usually be a [[Comparison]] but any [[Expression]] thrown in this syntactical place will be evaluated according to its [[Truthiness]].

The ternary version can be used when the [[Statement]] would be better handled as an [[Expression]], i.e. with a meaningful [[Return value]]:
```js
let foo = hitchhiker ? 42 : 3.1415;    // Assign result of ?: to a variable
console.log(hitchhiker ? 42 : 3.1415); // Pass result as argument
return hitchhiker ? 42: 3.1415;        // Return result
```
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)