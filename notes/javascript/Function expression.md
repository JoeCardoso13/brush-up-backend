Created: 2024-08-19 14:53

Here is the syntax, using an [[Anonymous function]]:
```js
let functionName = function(zeroOrMoreParameters...) {
  // function budy
};

greetPeople(args);
```
They can also be defined without an [[Anonymous function]]. Actually, any definition where the line doesn't start with the keyword `function` is a function expression. Examples:
```js
(function greetPeople() { // This is a function expression, not a declaration
  console.log("Good Morning!");
});

function makeGreeter(name) {
  return function greeter() { // Here the greeter is the function defined with an expression
    console.log(`Hello ${name}`);
  };
}
```
However, note that if a non-[[Anonymous function]] [[Expression]] is assigned to a [[Variable]], the [[Function]]'s name is available within its body, and the [[Variable]] outside of it:
```js
let hello = function foo() {
  console.log(typeof foo);   // function
};

hello();

foo();                       // Uncaught ReferenceError: foo is not defined
```

These **must** be defined before the [[Function call]].

Although they might look similar, a [[Function declaration]] behaves very differently than a function expression:
```js
function foo() {
  console.log('function declaration');
}

(function bar() {
  console.log('function expression');
});

foo();    // function declaration
bar();    // Uncaught ReferenceError: bar is not defined
```
Function expressions don't do [[Hoisting]].
## References
1. [ Intro to JS > Functions ](https://launchschool.com/books/javascript/read/functions#threewaystodefineafunction)