Created: 2024-08-19 10:00

JavaScript is an [[Object Oriented]] language. Objects are used to organize data. Typically, data [[Value]]s and the '[[Function]]s' that operate on those [[Value]]s are part of the same object.

JavaScript provides built-in [[Constructor function]]s, including `String`, `Array`, `Object`, `Math`, `Date`, and more. They can be used with the `new` keyword to create objects corresponding to the [[Literal form]] of their data [[Type]]:
```
> let a = new String('Hi')
> a
[String: 'hi']
> let b = new Number(13)
> b
[Number: 13]
```
This is something that JavaScript does "under the hood" when we call [[Method]]s with [[Primitive]] data [[Type]]s (that wouldn't naturally have access to them). This is called **auto boxing**. Example:
```js
let a = 'hi';                 // Create a primitive string with value "hi"
typeof a;                     // "string"; This is a primitive string value

let stringObject = new String('hi'); // Create a string object
typeof stringObject;          // "object"; This is a String object

a.toUpperCase();              // "HI" (auto-boxing takes place)
stringObject.toUpperCase();   // "HI"

typeof a;                     // "string"; The coercion is only temporary
typeof stringObject;          // "object"
```
---
There are various ways to [[Create object]]s.

The object data [[Type]] includes:
* Simple objects
* [[Array]]s
* [[Date]]s
* [[Function]]s

[[Object static method]]s provide a lot of useful functionality for JS programs.
## References
1. [ Intro to JS > Objects ](https://launchschool.com/books/javascript/read/objects#whatareobjects)