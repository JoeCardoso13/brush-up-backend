Created: 2024-11-14 16:08

Setters, like getters, are special methods you can define in any object. Internally, a setter looks like a concise syntax method definition preceded by the keyword `set`. A setter takes a single argument: the value you want to assign to the property. Outside of the method, however, it looks just like an ordinary property: you assign a value to what looks like a property in your object. You don't have to, nor can you, use the parentheses of a method call.

They are useful for validation purposes, i.e. to avoid unwanted [[Value]]s to be assigned to [[Object]] property's.
```js
class Student {
  #firstName;
  #lastName;
  #track;

  constructor(firstName, lastName, track) {
    this.#firstName = firstName;
    this.#lastName = lastName;

    switch (track) {
      case 'JavaScript':
      case 'Python':
      case 'Ruby':
        this.#track = track;
        break;
      default:
        throw new Error(`Invalid track: '${track}'`);
    }
  }

  set track(newTrack) {
    switch (newTrack) {
      case 'JavaScript':
      case 'Python':
      case 'Ruby':
        this.#track = newTrack;
        break;
      default:
        throw new Error(`Invalid track: '${newTrack}'`);
    }
  }
}

let student2 = new Student('Kay', 'Oakley', 'JavaScript');
console.log(`${student2.name.join(' ')} ${student2.track}`);
// Kay Oakley JavaScript

let student3 = new Student('Bill', 'Wisner', 'Python');
console.log(`${student3.name.join(' ')} ${student3.track}`);
// Bill Wisner Python

student3.track = 'Ruby';
console.log(`${student3.name.join(' ')} ${student3.track}`);
// Bill Wisner Ruby

student3.track = 'Baaa!';
console.log(`${student3.name.join(' ')} ${student3.track}`);
// Invalid track: 'Baaa!'
```

You can define setters in any object. You don't have to be using a class.
```js
let teacher = {
  firstName: 'Alan',
  lastName: 'Stone',

  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  },

  set name(nameArray) {
    this.firstName = nameArray[0]
    this.lastName = nameArray[1]
  },
};

teacher.name = ['Mike', 'Becker']
console.log(teacher.fullName);   // Mike Becker
```
## References
1. [JS OO Book > More Classes](https://launchschool.com/books/oo_javascript/read/more_classes)