Created: 2024-11-14 16:16

They are not available from the [[Class]] instances. **Static** **methods** typically provide utility [[Function]]s that perform tasks relevant to the [[Class]] but do not require access to instance-specific data.

A common use case for **static** **methods** is to report data relevant to a [[Class]]:
```js
class Student {
  static counter = 0;

  static showCounter() {
    console.log(`We have created ${Student.counter} students!`);
  }

constructor(name) {
    this.name = name;
    Student.counter += 1;
  }

}

let ken = new Student('Ken');
let lynn = new Student('Lynn');
Student.showCounter();        // We have created 2 students!
```
## References
1. [JS OO Book > More Classes](https://launchschool.com/books/oo_javascript/read/more_classes)