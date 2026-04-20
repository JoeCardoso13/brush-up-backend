Created: 2024-08-19 15:00

Coming in [[ES6]] they are a short-handed way for writing [[Function expression]]s when they're [[Anonymous function]]s.

The most contrived syntax is as follows:
```js
let functionName = () => console.log("Good Morning!");
functionName();
```
The parenthesis can be omitted if there's only 1 parameter. The example omits curly braces and the return [[Statement]] but they are necessary if the [[Function]]'s body has more than 1 line.

They're often used as [[Callback function]]s.

---
They do **not** have [[Function prototype]]s (but they do have [[Object prototype]]s just as any [[Object]] has):
```js
let foo = () => console.log('foo');
let fooProto = Object.getPrototypeOf(foo);

console.log(foo.prototype);                   // undefined
console.log(fooProto);                        // {}
console.log(fooProto === Function.prototype); // true
```

If their [[Function definition]] and [[Function call]] happens **within** a [[Method]], in the context of this outer [[Method call]], they'll get the [[Execution context]] from the [[Method call]] (i.e. [[this]] becomes attached to the [[Object]] caller), even though their invocation itself is a [[Function call]], not a [[Method call]]:
```js
let obj = {
  a: 'hello',
  b: 'world',
  foo() {
    let bar = () => console.log(this.a + ' ' + this.b);
    bar();
  }
};

obj.foo();
> hello world
```
This wouldn't happen if `bar` was defined in a [[Function declaration]] or [[Function expression]]. This is **especially important** when dealing with build-in JavaScript higher-order [[Function]]s that take a [[Function]] as argument, such as the case of the very often used [[forEach]] [[Array]] [[Method]] for instance.
## References
1. [ Intro to JS > Functions ](https://launchschool.com/books/javascript/read/functions#threewaystodefineafunction)