Created: 2024-11-14 10:40

They should be **capitalized** by convention, this tells the developer using it that they should call with [[new]].

```js
function Cat(name) {
  this.name = name;
}

let butterscotch = new Cat("Butterscotch");
let pudding = new Cat("Pudding");
```

Calling the `Cat` [[Function]] with the [[new]] keyword makes the call a constructor call. We also refer to `Cat` as a **constructor** **function** (remember: constructor [[Function]] is just a [[Function]] **intended** to be called with [[new]]). The `new` keyword performs several actions and returns an [[Object]] whose [[Type]] is the same as the [[Function]]'s name. Thus, `butterscotch` and `pudding` are **instances** of the `Cat` [[Type]].

You can also define [[Method]]s in a constructor function:

```js
function Cat(name) {
  this.name = name;

  this.purr = function() {
    console.log('purr');
  }

  this.speak = function() {
    console.log('meow!');
  }
}

let butterscotch = new Cat("Butterscotch");
butterscotch.purr();          // purr
butterscotch.speak();         // meow!

let pudding = new Cat("Pudding");
pudding.purr();               // purr
pudding.speak();              // meow!
```

[[Arrow function]]s **cannot** be constructor functions.

---
To [[Create object]]s using a constructor [[Function]] along with [[new]] keyword means they'll have a [[Type]]:
```js
function Foo() {
  this.foo = 42;
}

let obj = new Foo; // parenthesis can be omitted if no argument
console.log(obj instanceof Foo); // true
console.log(obj.constructor);    // [Function: Foo]
```
## References
1. [ OO JS book > Objects ](https://launchschool.com/books/oo_javascript/read/types_and_objects)