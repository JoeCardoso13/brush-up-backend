Created: 2024-11-15 09:47

This pattern to [[Create object]] **maps** the [[Class]] syntactic sugar into JavaScript's build-in [[Prototypal inheritance]] model. 

Using the following [[Class]]-based code as an example:
```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() {
    console.log(`${this.name} is eating.`);
  }
}

class Mammal extends Animal {
  constructor(name, hasFur) {
    super(name);
    this.hasFur = hasFur;
  }

  sleep() {
    console.log(`${this.name} is sleeping.`);
  }
}

class Dog extends Mammal {
  constructor(name, hasFur, breed) {
    super(name, hasFur);
    this.breed = breed;
  }

  bark() {
    console.log(`${this.name} the ${this.breed} ` +
                'is barking.');
  }
}

let myDog = new Dog('Rex', true, 'German Shepherd');
myDog.eat();    // Rex is eating.
myDog.sleep();  // Rex is sleeping.
myDog.bark();   // Rex the German Shepherd is barking.
```
To map it into the JS's native [[Prototypal inheritance]] model we do it in 5 steps:
1) Replace the [[Class]]es definitions along with the content from their constructor [[Method]]s definitions for [[Constructor function]]s with the same name.
2) For every [[Class]] that inherits (extends) from another [[Class]], i.e. a sub-[[Class]] or sub-[[Type]], we use the [[Object static method]] `Object.create(SuperClass.prototype)` to connect the current [[Constructor function]] `prototype` **property** to the [[Function prototype]] of its super-[[Class]]. This means we are **reassigning** the current [[Constructor function]]'s [[Function prototype]].
3) Because we **reassigned** the [[Function prototype]] of our sub-[[Type]]s, we need/should wrap up their [[Function prototype]]'s `constructor` **properties** to themselves, as this is standard and expected in using JS's libraries. 
4) Add all instance [[Method]]s from the [[Class]]es to the [[Function prototype]] of the respective [[Constructor function]].
5) Finally, to replace the use of `super` from the [[Class]] definition syntax of the sub-[[Class]]es, we use `Function.prototype.call` passing [[this]] followed by all arguments that the super-[[Class]] takes in the **1st line** of every sub-[[Class]] [[Constructor function]].
```js
function Animal(name) {
  this.name = name;
}

Animal.prototype.eat = function () {
  console.log(`${this.name} is eating.`);
}

function Mammal(name, hasFur) {
  Animal.call(this, name);
  this.hasFur = hasFur;
}

Mammal.prototype = Object.create(Animal.prototype);
Mammal.prototype.constructor = Mammal;

Mammal.prototype.sleep = function () {
  console.log(`${this.name} is sleeping.`);
}

function Dog(name, hasFur, breed) {
  Mammal.call(this, name, hasFur);
  this.breed = breed;
}

Dog.prototype = Object.create(Mammal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function () {
  console.log(`${this.name} the ${this.breed} ` + 'is barking.');
}

let myDog = new Dog('Rex', true, 'German Shepherd');
myDog.eat();    // Rex is eating.
myDog.sleep();  // Rex is sleeping.
myDog.bark();   // Rex the German Shepherd is barking.
```
## References
1. [ JS OO Book > Prototypal Inheritance ](https://launchschool.com/books/oo_javascript/read/prototypal_inheritance#constructorprototypepattern)