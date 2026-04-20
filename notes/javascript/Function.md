Created: 2024-08-19 14:47

In JavaScript, all functions are **first-class functions**.

They have 3 forms of [[Function definition]]:

 * [[Function declaration]]
 * [[Function expression]]
 * [[Arrow function]]

They all (even the [[Function declaration]]) generate a [[Variable]] with their own name. [[Function declaration]]s and [[Function expression]]s can be used as a [[Constructor function]] whereas [[Arrow function]]s cannot.

JavaScript is very loose when it comes to [[Arity]], or, put differently, it doesn't have it.

Without a `return` [[Statement]] (or if it doesn't include a [[Value]]), functions have, by default, [[Undefined]] as their [[Return value]].

In JS functions are just [[Object]]s. Therefore they can be handled as such:
```js
function startle() {
  console.log('Yikes!');
}

let surprise = startle;
surprise(); // logs: Yikes!
```
## References
1. [ Intro to JS > Functions ](https://launchschool.com/books/javascript/read/functions#threewaystodefineafunction)