Created: 2024-08-19 11:52

Variables are declared with `let`, `const` or `var`. The location of the variable declaration (and its type) determines the [[Variable scope]]. JavaScript is dynamically typed, so a [[Variable]] declaration doesn't specify a [[Type]] and any [[Variable]] can point to any data [[Type]] and have [[Variable (re)assignment]] to any other [[Type]] at any time.

Declarations can be concatenated like so:
```js
let a = 1, b = 2;
```

Declaring a `var` [[Variable]] at the top level of a program creates a property on the [[Global object]] (1):
```js
// Use the Node REPL for this example.
// Type the commands one at a time - don't use copy and paste.

var bar = 42;
console.log(global.bar); // 42
bar += 1;
console.log(global.bar); // 43

let foo = 86;
console.log(global.foo); // undefined
```

In a [[Variable (re)assignment]] [[Expression]], JS travels from the **local** [[Variable scope]] to the surrounding scope looking for its **declaration** until it reaches the **Global** **Scope**. If it can't find a corresponding **variable** **declaration**, it makes the [[Variable]] available globally by attaching it to the [[Global object]]. (1)

They are often declared and "assigned" simultaneously:
```js
> let firstName = 'Mitchell'
> firstName
'Mitchell'
```
When this happens we usually don't say they're being assigned, but **initialized** to a [[Variable]]. The [[Expression]] to the right of `=` (assignment operator) is the **initializer**. If they are **only** declared, then they are being **initialized** to **no** [[Value]].

`const` is similar to `let` but their [[Value]]s can never undergo [[Variable (re)assignment]]. The [[Style guide]] recommends it to be uppercase in some cases.

(1) [[Variable (re)assignment]] in the absence of that [[Variable declaration]], although **very similar** to declaring a `var` [[Variable]] at the **top level** of the program, in terms of what it does to the [[Global object]], has a subtle but significant difference: _you can delete global variables that you don't declare, but not those that you did._ Example (running on a browser):
```js
foo = 1;
var moreFoo = 3;

function bar() {
  return 7;
}

delete window.foo;         // deleted
delete window.moreFoo;     // not deleted
delete window.bar;         // not deleted

console.log(window.bar());                         // 7
console.log(window.foo);                           // undefined
console.log(window.hasOwnProperty("foo"));         // false
console.log(window.moreFoo);                       // 3
```

---
`var` and `let` declarations can have strikingly **different** behaviors. The former can be **re-declared** at will, while the latter throws an error if attempted:
```
> var b = 13;
> var b = 12; // No problem here
> let c = 13;
> let c = 12; // Uncaught SyntaxError: Identifier 'c' has already been declared
```
Be careful, the same is true for [[Function]]s:
```js
let counter = 5; 
let rate = 3;

function counter(count) {
  // ...
}
// Very different if counter and rate were declared by var
console.log('The total value is ' + String(counter * rate));
```
## References
1. [ Intro to JS > Variables ](https://launchschool.com/books/javascript/read/variables)