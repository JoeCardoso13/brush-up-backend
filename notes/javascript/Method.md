Created: 2024-08-22 10:15

When [[Function]]s are part of [[Object]]s, we call them methods. They are properties (names, keys) of the [[Object]] and are called with dot notation. They take parenthesis and arguments just like any [[Function call]].

Examples:
```js
(5.234).toString();       // "5.234"
'pizza'.match(/z/);       // [ "z", index: 2, input: "pizza" ]
Math.ceil(8.675309);      // 9
Date.now();               // 1467918983610
```

They can be custom-made when we [[Create object]]s in [[Literal form]] by having the [[Function definition]] as the [[Value]] of the property (key-value pair). This allows for the method to have access to the caller [[Object]] data at **execution time** through [[this]] keyword.

---
Be aware that they can be delegated/inherited and still be considered an instance method of the [[Object]]. I.e. no matter where they are found in the [[Prototype chain]], they are considered methods of the [[Object]] regardless of the fact that they may also be methods of an [[Object prototype]]. Indeed, the only way to disambiguate their origin is using one of the [[Object static method]]s.
## References
1. [ courses > JS210 > lesson 5 > Intro ](https://launchschool.com/lessons/79b41804/assignments/091246c3)