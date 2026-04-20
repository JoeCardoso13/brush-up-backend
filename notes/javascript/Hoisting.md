Created: 2024-08-20 19:57

JavaScript engines operate in two main phases: a **creation phase** and an **execution phase**. The execution phase is when the program runs code line-by-line. That's what most people mean when they talk about a program's execution. However, before the execution phase begins, the creation phase does some preliminary work. One of those work items is to find all of the [[Variable declaration]]s, [[Function declaration]]s, and class _declarations_. That action seems to move the declarations to the top of their respective [[Function]] or [[Block]]: function-scoped declarations get moved to the top of the [[Function]], and block-scoped declarations get moved to the top of the [[Block]]. This process is called **hoisting**.

#### Variable Hoisting
* [[Variable declaration]]s with `var` get hoisted:
```js
console.log(bar); // undefined
var bar = 3;
console.log(bar); // 3
```
* [[Variable declaration]]s with `let` and `const` go to the **Temporal Dead Zone** (**TDZ**):
```js
console.log(foo); // ReferenceError: Cannot access 'foo' before initialization
let foo;
console.log(qux); // ReferenceError: Cannot access 'qux' before initialization
const qux = 42;
```
Note that in a way, these `let` and `const` declarations **do** get hoisted. The message differs if they're not declared at all:
```js
console.log(baz); // ReferenceError: baz is not defined
```

#### Function Definition Hoisting
* [[Function declaration]]s are hoisted in whatever scope they're in (\*). It's as if the whole body had lifted to the top of the scope:
```js
console.log(hello());

function hello() {
  return 'hello world';
}
```
Is equivalent to:
```js
function hello() {
  return 'hello world';
}

console.log(hello());      // logs "hello world"
```
(\*) Except for [[Block]] scope. JavaScript is inconsistent in the results and can't handle the case of a [[Function declaration]] inside a [[Block]]. The following snippet is an example of what you should **never** do:
```js
function foo() {
  if (true) {
    function bar() {
      console.log("bar");
    }
  } else {
    function qux() {
      console.log("qux");
    }
  }

  console.log(bar);
  bar();

  console.log(qux);
  qux();
}

foo();
```
* [[Function expression]]s obey the [[Variable]] hoisting rules when are being assigned to a [[Variable]].
#### Variable vs Function Hoisting
A [[Function declaration]] will be hoisted above the `var` [[Variable declaration]] when both exist:
```js
bar();              // logs undefined
var foo = 'hello';

function bar() {
  console.log(foo);
}
// Hoisted version:
function bar() {
  console.log(foo);
}

var foo;

bar();          // logs undefined
foo = 'hello';
```
If [[Variable]] and [[Function]] have the same name, the [[Variable declaration]] gets redundant:
```js
bar();             // logs "world"
var bar = 'hello';

function bar() {
  console.log('world');
}
// Hoisted version:
function bar() {
  console.log('world');
}

bar();
bar = 'hello';
```
`let` and `const` declarations have built-in mechanisms to avoid these problems:
```js
let foo = 3;
function foo() {}; // SyntaxError: Identifier 'foo' has already been declared
```
```js
function foo() {};
let foo = 3;  // SyntaxError: Identifier 'foo' has already been declared
```
## References
1. [ courses > JS210 > lesson 2 > Functions and Variable Scope ](https://launchschool.com/lessons/7cd4abf4/assignments/510e62bb)