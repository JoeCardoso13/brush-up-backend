Created: 2024-08-19 11:52

Is how a [[Value]] from a pre-existing [[Variable]] is changed.

In a [[Variable (re)assignment]] [[Expression]], JS travels from the **local** [[Variable scope]] to the surrounding scope looking for its **declaration** until it reaches the **Global** **Scope**. If it can't find a corresponding **variable** **declaration**, it makes the [[Variable]] available globally by attaching it to the [[Global object]]. Therefore if a [[Variable]] is attempted to be reassigned while it never been through [[Variable declaration]], JS automatically initializes the [[Variable]], adds it as a property of the global [[Object]] and the [[Variable]] will have global [[Variable scope]], which is almost **never** desired.

Be mindful that for the process described above to happen, *the pseudo-assignment (actual initialization) code has to be executed*. The following examples generates error:
```js
console.log(a); // Uncaught ReferenceError: a is not defined

function hello() {
  a = 1;
}

if (false) {
  b = 1;
}

console.log(b); // Uncaught ReferenceError: b is not defined
```
## References
1. [ Intro to JS > Variables ](https://launchschool.com/books/javascript/read/variables)