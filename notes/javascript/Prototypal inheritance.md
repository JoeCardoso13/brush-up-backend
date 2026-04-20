Created: 2024-11-14 16:35

When we try to access a **property** or a [[Method]] on an [[Object]], JavaScript searches not only in the [[Object]] itself, but all the [[Object]] on its [[Prototype chain]], until the end is reached. This doesn't affect the [[Execution context]] and [[Value]] of [[this]]:
```js
let foo = {
  hello() {
    return 'hello ' + this.name;
  },
};

let bar = Object.create(foo);
bar.name = 'world';
bar.hello();          // returns hello world
```
This also allows for a more **efficient** pattern to [[Create object]]s than [[Object factory]] because, instead of duplicating [[Method]]s every time we create a new [[Object]], we keep the single [[Method]] available through [[Inheritance]] in the [[Prototype chain]] and only duplicate references to it.

**Prototypal inheritance** is a core feature in JavaScript. [[Object]]s can inherit properties and [[Method]]s directly from other [[Object]]s, known as **prototypes**, rather than from [[Class]]es. This approach differs from the classical [[Inheritance]] model used in most other [[Object Oriented]] languages. It provides more **flexible** and **dynamic** object creation and modification, enabling [[Object]]s to share behavior by referencing a **prototype object**. Looking from bottom-up perspective, instead of top-down, we can say, alternatively, that the [[Inheritance]] of [[Method]]s is the delegation of these [[Method]]s from [[Object]]s below the hierarchy to [[Object prototype]]s above.  **Behavior delegation** is **prototypal inheritance** viewed from bottom-up.

(prototypes may contain ordinary properties, however, the vast majority of prototypes only contain methods)

There are 2 kinds of **prototype** **objects**:
* [[Function prototype]]
* [[Object prototype]]
---
The [[Inheritance]] is defined at the moment the [[new]] [[Object]] is created (**not** at execution time). The following demonstrates:
```js
let ninja;
function Ninja() {
  this.swung = true;
}

ninja = new Ninja(); // prototypal inheritance was defined here!

Ninja.prototype = {
  swingSword: function() {
    return this.swung;
  },
};

console.log(ninja.swingSword()); // raise error!
```
---
#### [[Inheritance]] for instance [[Method]]s 
When we [[Create object]] using [[new]], the [[Object prototype]] of the created [[Object]] is, by default, identical to the [[Function prototype]] of the [[Object]]'s [[Constructor function]].

Since [[Function]]s are [[Object]]s and all [[Object]]s have [[Object prototype]]s, even [[Function prototype]]s have an [[Object prototype]]. By default it is the [[Function prototype]] of its super[[Class]]. With almost all [[Object]]s, you can follow this "chain" of [[Object prototype]]s all the way back to a **prototype** **object** called `Object.prototype`. This chain is called the [[Prototype chain]]. The [[Object prototype]] of the `Object.prototype` [[Function prototype]] is `null`.

#### [[Inheritance]] for [[Static method]]s
[[Function]]s and [[Class]]es are also [[Object]]s and, as such, have a [[Prototype chain]] from which their [[Static method]]s is searched by JS for [[Inheritance]] purposes. This is defined by their own [[Object prototype]] _that is completely separate/independent from their [[Function prototype]]_ (used to establish the [[Inheritance]] of their instantiated [[Object]]s as described above).

The [[Object prototype]]s for [[Function]]s and [[Class]]es ultimately chain to `Function.prototype`, which has some useful [[Method]]s such as `apply`, `call`, and `bind`.
## References
1. [JS OO Book > Prototypal Inheritance](https://launchschool.com/books/oo_javascript/read/prototypal_inheritance)