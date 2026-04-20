Created: 2024-08-19 14:52

They must **always** have a name, i.e. can't be [[Anonymous function]]s.

A function declaration differentiates from [[Function expression]] primarily due to beginning the [[Statement]] with the `function` keyword. They **always** begin have `function` keyword beginning the line they're in. They're also the only form of [[Function definition]] that creates a property in the [[Global object]] (like a `var` [[Variable declaration]]) if at the program's **top level**.

They have the following structure:

- The `function` keyword
- The **name** of the [[Function]]
- A list of comma separated parameters
- A block of statements (the function body)

The syntax is as follows:
```js
function functionName(zeroOrMoreParameters...) {
  // function body
}

functionName(args);
```
These **can** be called before declaring, due to [[Hoisting]].

They automatically generate a corresponding [[Variable]] with their name. For real:
```js
> function hello() {
... console.log('hello');
... }
> typeof hello
= 'function'
> let hey = hello
> hey()
hello
> hello = 'hi'
> console.log(hello)
'hi'
> console.log(hey)
[Function: hello]
```
## References
1. [ Intro to JS > Functions ](https://launchschool.com/books/javascript/read/functions#threewaystodefineafunction)