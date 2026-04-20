Created: 2024-08-19 11:57

Defined by the [[Variable declaration]].

A [[Variable]]'s scope is the part of the program that can access that [[Variable]] by name. [[Variable]] scoping rules describe how and where the language finds and retrieves [[Value]]s from previously declared variables. In JavaScript, every [[Function]] or [[Block]] creates a **new** variable scope.

The initial scope, outside of any [[Function]] or [[Block]], is the **Global** **Scope**. [[Variable]]s in this scope are available from their [[Variable declaration]] to the end of the program. Any [[Function]] or [[Block]] will define a **Local** **Scope** within them. Inside a **Local** **Scope** we can access [[Variable]]s from the **Global** **Scope** but **not** vice-versa. These scopes can be nested inside each other, but the same principle always applies. 

At any point in a JavaScript program, there is a hierarchy of scopes from the **local** **scope** of the code up to the program's **global** **scope**. When resolving any [[Variable]], JS goes through this hierarchy in order. This means that a [[Variable]] in a **local** **scope** can shadow another [[Variable]] of the same name in an outer scope. The way JavaScript moves through this hierarchy of scopes to resolve a [[Variable]] is define by the [[Closure]].

[[Variable]]s declared with `let` or `const` have [[Block]] scope, which is obviously a subset of [[Function]] scope.

[[Block]] scope example:
```js
if (1 === 1) {
  let a = 'foo';
}

console.log(a); // ReferenceError: a is not defined
```
They can be parallel:
```js
const FOO = 'bar';
{
  const FOO = 'qux';
}

console.log(FOO); // bar
```

---
[[Variable]]s declared with `var` have [[Function]] scope.

[[Function]] scope example:
```js
function foo() {
  if (true) {
    var a = 1;
    let b = 2;
  }

  console.log(a); // 1
  console.log(b); // ReferenceError: b is not defined
}

foo();
```
## References
1. [ Intro to JS > Variables ](https://launchschool.com/books/javascript/read/variables)