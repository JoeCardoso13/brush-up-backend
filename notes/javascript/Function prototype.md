Created: 2024-11-14 16:46

A.K.A. constructor's prototype object.

Most of JavaScript [[Class]]es and [[Function]]s automatically have a `prototype` **property** that references their **function prototype**. They are used when creating [[new]] [[Object]]s from the [[Class]] or [[Constructor function]]. The newly created [[Object]] is given a reference to the **function prototype**. This reference is called the [[Object prototype]].

They have, themselves, a `constructor` property that references its [[Function]], i.e. the [[Class]]/[[Function]] from which it is a `prototype` property of.

Since we can access the **function prototype** easily through the `prototype` **property** of [[Function]]/[[Class]]es, we can manipulate it at will:
```js
class Animal {}

Animal.prototype.foo = function() {
  console.log('this is foo');
};

Animal.prototype.bar = function() {
  console.log('this is bar');
};

console.log(Animal.prototype);
// { foo: [Function (anonymous)],
//   bar: [Function (anonymous)] }

function Vehicle() {}

Vehicle.prototype.drive = function() {
  console.log('off we go');
};

console.log(Vehicle.prototype);
// { drive: [Function (anonymous)] }
```

[[Arrow function]]s do **not** have them (however they do have [[Object prototype]] just as any [[Object]] has).
## References
1. [JS OO Book > Prototypal Inheritance](https://launchschool.com/books/oo_javascript/read/prototypal_inheritance)