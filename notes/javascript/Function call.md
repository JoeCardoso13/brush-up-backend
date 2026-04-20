Created: 2024-08-19 12:56

A.K.A. [[Function invocation]]

Is how to use the code contained in a [[Function definition]]'s body. Arguments can be passed as [[Object]]s and/or [[Primitive]]s in [[Literal form]] or using a [[Variable]] as reference to them. Their [[Return value]] is given by the return [[Statement]] in the [[Function definition]] or is [[Undefined]].

You call a [[Function]] by appending parenthesis to its name. A [[Function]] call basic syntax is:
```js
myFunction(args);
```
The name(s) between parenthesis in a function call are the **arguments**.

The function call will run the code contained in the body of the [[Function definition]] until it reaches a return [[Statement]], whereby it exits and returns the [[Return value]] of that [[Statement]].

Functions designed to always return a [[Boolean]] are called *predicates*.

A function call and its [[Return value]] can behave as **Pass** **By** **Reference** or **Pass** **By** **Value** in Java Script. [[Primitive]] [[Value]]s always behave as the latter, while [[Object]]s can behave as both, they're said the be passed **By** **Reference** when **mutated** and **By** **Value** when their [[Variable]] is reassigned.
## References
1. [ Intro to JS > Functions & Scope ](https://launchschool.com/books/javascript/read/functions#functionsscope)