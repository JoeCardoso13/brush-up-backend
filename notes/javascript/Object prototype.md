Created: 2024-11-14 16:49

All JavaScript [[Object]]s have an **object prototype**. The **object prototype** is where JavaScript looks for **inherited** [[Method]]s:
```js
class Cat {
  constructor(name, color) {
    this.name = name;
    this.color = color;
  }

  whoAmI() {
    console.log(`My name is ${this.name}.`,
                `\nI am a ${this.color} cat.`);
  }
}

let cheddar = new Cat('Cheddar', 'ginger');
let cheddarProto = Object.getPrototypeOf(cheddar);

console.log(Object.getOwnPropertyNames(cheddarProto)); // ['constructor', 'whoAmI'];
```

Both ordinary [[Object]]s and [[Function]]s/[[Class]]es will have JS looking for their **object prototype** to find inherited [[Method]]s, instance [[Method]]s for the former and [[Static method]]s for the latter. In other words, the **object prototype** is how the parallel [[Prototype chain]]s for both instance and [[Static method]]s are defined.
## References
1. [JS OO Book > Prototypal Inheritance](https://launchschool.com/books/oo_javascript/read/prototypal_inheritance)