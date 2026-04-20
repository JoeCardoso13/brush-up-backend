Created: 2024-11-14 17:21

When we [[Create object]] from its [[Literal form]], we create an instance of the [[Object]] [[Class]]. Therefore the [[Object prototype]] of the created [[Object]] is the `Object.prototype` [[Function prototype]]. This is the cause of one of the disadvantages of using the [[Object factory]] pattern. [[Object]]s created with [[new]] keyword are no different though:
```js
let obj = new Object();
let objProto = Object.getPrototypeOf(obj);
console.log(objProto === Object.prototype); // true
```

To access the **prototype chain**, i.e. set and retrieve [[Object prototype]]s from [[Object]]s, we use a couple of [[Object static method]]s: `Object.getPrototypeOf(obj)` and `Object.setPrototypeOf(obj)`. They substitute the deprecated `__proto__` (pronounce dunder proto). Under the hood these deal with a **hidden** property of every [[Object]], the `[[Prototype]]`, that points to its [[Object prototype]] but can't be accessed directly.

Be aware that while the [[Object]] [[Static method]] `Object.getPrototypeOf` returns only the immediate [[Object prototype]] from an [[Object]], the instance [[Method]] `Object.prototype.isPrototypeOf` checks the whole **prototype chain**.

[[Function]]s and [[Class]]es have their own, parallel, separate and independent **prototype chain** for [[Prototypal inheritance]] of their [[Static method]], except for [[Arrow function]]s that do **not** have them.
## References
1. [JS OO Book > Prototypal Inheritance](https://launchschool.com/books/oo_javascript/read/prototypal_inheritance)