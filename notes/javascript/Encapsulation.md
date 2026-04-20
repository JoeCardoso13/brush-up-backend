Created: 2024-11-14 11:45

It's the idea of bundling or combining data and the behaviors of that data/state into a single entity, e.g., an object. For example:

```js
let cocoa = {
  animalType: 'cat',
  name: 'Cocoa',

  purr: function() {
    console.log('Purr');
  },

  info: function() {
    console.log(`My name is ${this.name}. I am a ${this.animalType}.`)
  }
}

cocoa.purr();       // Purr
cocoa.info();       // My name is Cocoa. I am a cat.
```

It lets the programmer think about things with a new level of abstraction.

Until very recently this was all that Encapsulation meant in JavaScript [[Object Oriented]] context. However, [[ES13]] facilitated the provision for **access restriction** with [[Private field]]s and [[Private method]]s which means that Encapsulation can now be thought of in terms of public vs private interface for interacting with [[Object]]s.
## References
1. [ OO Book > Object Model ](https://launchschool.com/books/oo_javascript/read/the_object_model)