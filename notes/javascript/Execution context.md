Created: 2024-11-16 10:55

All JavaScript code executes within a **context**. The **top-level context** in a **web browser** is the `window` object. All global [[Method]]s and [[Object]]s (such as `parseInt` or `Math`) are **properties** of this [[Object]]. In **Node**, the top-level context is called `global`. However, be aware that **Node** has some peculiarities that cause it to behave differently from **browsers**.

The **execution context**'s rules work in a fundamentally different way from scoping rules are determined because _JavaScript uses [[Lexical scoping]] for these, whereas the rules for determining [[this]] are taken at **execution time**_
#### Implicit execution context for [[Function]]s
It's the [[Object]] referred by [[this]] when [[Function call]] happens at the **top level** - [[Global object]] - except when [[Strict mode]] is enabled.

It can be `window`, `global`, empty [[Object]] or `undefined`, depending on how the program is run.
#### Implicit execution context for [[Method]]s
It's the [[Object]] that called the [[Method]] or the [[Global object]] in the case of a [[Function call]].

Being given at **execution time** means that:
```js
let foo = {
  bar() {
    return this;
  },
};

let baz = foo.bar;

baz() === foo;    // false
baz() === window; // true
```

Be aware that a [[Function call]] inside a [[Method]] call still have the [[Global object]] as the **implicit** execution context:
```js
let obj = {
  a: 'hello',
  b: 'world',
  foo() {
    function bar() {
      console.log(this.a + ' ' + this.b);
    }

    bar();
  },
};

obj.foo(); // undefined undefined
```
This trap is insidious and well-known. Most developers consider it to be a mistake in the language design. We can tackle the problem by:
* Making up a variable `self` to capture [[this]] the [[Closure]] of the [[Function]] and use it instead of [[this]]. 
* Making the **execution context** explicit or hard bound, as shown below.
* Using [[Arrow function]].
#### Explicit execution context
The [[Function prototype]] of all [[Function]]s has some interesting [[Method]]s inherited by all [[Function]]s (a [[Method]] is just a [[Function]] called by an [[Object]]) that lets us establish a desired **execution context** at **execution time**. When we do so, we are create an _explicit execution context_.

The [`Function.prototype.call`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)  and the [`Function.prototype.apply`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply):
```js
someObject.someMethod.call(context, arg1, arg2, arg3, ...);
someObject.someMethod.apply(context, [arg1, arg2, arg3, ...]);
```
Use this mnemonic to help remember what each method does:
- **C**all: **C**ount the **C**ommas (you have to count the number of arguments to match the called function)
- **A**pply: **A**rguments as **A**rray

There is a way to 'hard bind' an **execution context** to a [[Function]] using one of the [[Method]]s provided by `Function.prototype` [[Function prototype]], the [`Function.prototype.bind`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind): 
```js
let object = {
  a: 'hello',
  b: 'world',
  foo() {
    return this.a + ' ' + this.b;
  },
};

let bar = object.foo;
bar();                                // "undefined undefined"

let baz = object.foo.bind(object);
baz();                                // "hello world"

let object2 = {
  a: 'hi',
  b: 'there',
};

baz.call(object2);  // "hello world" - `this` is still `object`
```
Unlike `call` or `apply`, `bind` doesn't execute the [[Function]] that invokes it. Instead, it creates and returns a **new** [[Function]] (it does **not** mutate the original) that **permanently** binds the invoking [[Function]] to a given **context** [[Object]]. Thus, we can pass the returned function around without concern that its **context** will change.

When we say that the **new** [[Function]] returned by `bind` is **permanently** bound, we mean it:
```js
let obj = {
  a: 'Amazebulous!',
};
let otherObj = {
  a: "That's not a real word!",
};

function foo() {
  console.log(this.a);
}

let bar = foo.bind(obj);

bar.call(otherObj);
```
## References
1. [ JS225 > Function Context and Objects ](https://launchschool.com/lessons/c9200ad2/assignments/4cc36fd6)