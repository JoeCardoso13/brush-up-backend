Created: 2024-11-14 16:53

When we call a [[Constructor function]] with the `new` keyword, JavaScript takes the [[Function prototype]] of the [[Constructor function]] (an [[Object]] referenced by the [[Function]]'s prototype property, e.g. `MyFunction.prototype`) and assigns it as the [[Object prototype]] of the new [[Object]] created by the [[Constructor function]] (referenced by [[this]] inside the [[Function definition]]). Thus, an [[Object prototype]] is, by default, identical to the [[Function prototype]] of the [[Object]]'s [[Constructor function]].

The use of new always set [[this]] to be the newly created, empty [[Object]]. This [[this]] [[Object]] is implicitly returned. If the [[Return value]] intended is otherwise, attention is needed:
```js
function Person(firstName, lastName) {
  if (!lastName) {
    return 'Please provide a last name';
  }

  this.firstName = firstName;
  this.lastName = lastName;
  this.fullName = function() {
    return (this.firstName + ' ' + this.lastName).trim();
  };
}

let noLastName = new Person('John');
console.log(noLastName);   // logs an instance of a Person object
console.log(noLastName instanceof Person); // => true
```
This can be solved by returning an [[Object]] (other than [[this]]) instead of a [[String]]:
```js
function Person(firstName, lastName) {
  if (!lastName) {
    return { invalidInput: 'Please provide a last name' };
  }

  this.firstName = firstName;
  this.lastName = lastName;
  this.fullName = function() {
    return (this.firstName + ' ' + this.lastName).trim();
  };
}

let noLastName = new Person('John');
console.log(noLastName);   // => { invalidInput: 'Please provide a last name' };
console.log(noLastName instanceof Person); // => false
```
## References
1. [JS OO Book > Prototypal Inheritance](https://launchschool.com/books/oo_javascript/read/prototypal_inheritance)