Created: 2024-11-14 16:13

They are **properties** that are defined on the [[Class]] itself. They are not tied to an instance of the class. A common use case for static fields is to keep track of something related to a [[Class]], such as an instance count:
```js
class Student {
  static counter = 0;

  constructor(name) {
    this.name = name;
    Student.counter += 1;
  }
}

console.log(Student.counter);           // 0

let ken = new Student('Ken');
console.log(Student.counter);           // 1

let lynn = new Student('Lynn');
console.log(Student.counter);           // 2
```

Or, using [[Prototype pattern]] syntax:
```js
	ifunction Dog(name, breed, weight) {
  this.name = name;
  this.breed = breed;
  this.weight = weight;
  Dog.allDogs.push(this);
}

Dog.species = "Canis lupus";
```
Here `allDogs` and `species` are static properties/fields.
## References
1. [JS OO Book > More Classes](https://launchschool.com/books/oo_javascript/read/more_classes)