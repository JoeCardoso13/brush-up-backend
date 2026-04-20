Created: 2024-08-19 11:34

They are a reference to a [[Value]].

They may refer to several things:

- Variable names declared by `let` and `var`
- Constant names declared by `const`
- Properties of the global [[Object]]
- [[Function]] names
- [[Function]] parameters
- Class names
They do **not** refer to simple [[Object]] properties/names/keys. They are almost synonymous with **Identifier** (the only difference is that the latter includes properties of [[Object]]s, in general, as well).

The lifecycle of a variable is to undergo [[Variable declaration]] and [[Variable (re)assignment]](s) in this order.

[[Variable scope]] determines where the variable is available in the program. It determines whether a variable is a [[Global variable]] or [[Local variable]].

---
Variable names:
* Must not be a [reserved word](https://262.ecma-international.org/5.1/#sec-7.6.1.1).
* Must not start with a [[Number]].
* Must start with Unicode letter, an underscore (`_`) or a dollar sign (`$`).
## References
1. [ Intro to JS > Variables ](https://launchschool.com/books/javascript/read/variables)