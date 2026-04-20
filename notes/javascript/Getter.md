Created: 2024-11-14 16:03

Getters are a special kind of method you can define in any object. Internally, they look like methods with the keyword `get` preceding a method definition that uses concise method syntax. However, getters aren't used like methods. Instead, they are used like ordinary instance properties: you reference the getter name to retrieve the corresponding data. You don't have to, nor can you, use the parentheses of a method call.

You can define getters in any object. You don't have to use a class. For instance, in the code below, we've defined a getter to make it easy to get the full name:
```js
let teacher = {
  firstName: 'Alan',
  lastName: 'Stone',

  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  },
};

console.log(teacher.fullName);   // Alan Stone
```

Consider another use case for getters. Suppose your object has a property whose value is mutable. Suppose you allow direct access to that property. In that case, users can modify the mutable value, which may be undesirable. In that case, you can write a getter that returns a copy of the mutable property's value:
```js
let teacher = {
  firstName: 'Alan',
  lastName: 'Stone',
  _students: ['Pete', 'Brian', 'Andrea', 'Beverly', 'Joel'],

  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  },

  get students() {
    return [...this._students];  // A copy of the _students array
  },
};

console.log(teacher.fullName);   // Alan Stone

let students = teacher.students;
console.log(students);
// [ 'Pete', 'Brian', 'Andrea', 'Beverly', 'Joel' ]

students.pop();
console.log(students);
// [ 'Pete', 'Brian', 'Andrea', 'Beverly' ]

console.log(teacher.students);
// [ 'Pete', 'Brian', 'Andrea', 'Beverly', 'Joel' ]
```
By returning a copy of the `_students` array, we can manipulate the return value without impacting the `teacher` object.

Note that we had to change the name of the `students` property to `_students`. If you don't do this, you'll experience a stack overflow due to recursive calls to the `students` getter. A single leading underscore is a JavaScript convention that marks something as intended for internal use only. So, while users can use either `teacher.students` or `teacher._students` to access the `_students` property, they should only use `teacher.students`.

Instead of the single underscore, you can also use private fields:
```js
class Student {
  #firstName;
  #lastName;
  #track;

  constructor(firstName, lastName, track) {
    this.#firstName = firstName;
    this.#lastName = lastName;
    this.#track = track;
  }

  get name() {
    return [this.firstName, this.lastName];
  }

  get firstName() {
    return this.#firstName;
  }

  get lastName() {
    return this.#lastName;
  }

  get track() {
    return this.#track;
  }
}
```
## References
1. [JS OO Book > More Classes](https://launchschool.com/books/oo_javascript/read/more_classes)