Created: 2024-11-14 14:39

**Polymorphism** is the ability of different data [[Type]]s to respond to a common interface. For instance, if we have a [[Function]] or [[Method]] that invokes the `move` [[Method]] on the [[Object]] passed to it as an argument, we can pass the [[Function]] or [[Method]] any argument that has a compatible `move` [[Method]]. The [[Object]] might represent a human, a cat, a jellyfish, or, conceivably, even a car, planet, or train. **Polymorphism** lets us use the same [[Method]] invocation for many different [[Object]] [[Type]]s. In such cases, the [[Function]] or [[Method]] is considered **polymorphic**.

```js
let cat = {
  move() {
    console.log("The cat is walking");
  },
};

let planet = {
  move() {
    console.log("The planet is revolving around the Sun");
  },
}

for (let item of [cat, planet]) {
  item.move();
}

// The cat is walking
// The planet is revolving around the Sun
```
## References
1. [ OO Book > Object Model ](https://launchschool.com/books/oo_javascript/read/the_object_model)