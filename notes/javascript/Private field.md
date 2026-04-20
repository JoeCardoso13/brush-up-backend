Created: 2024-11-14 15:50

Private fields are accessed like instance properties, except the name of the property is prefixed by a `#` character. In addition, you must declare (and optionally initialize) the field at the class level:
```js
class Foo {
  // Next 2 lines declare #data and #initializedData fields
  #data;                      // uninitialized private field
  #initializedData = 43;      // initialized private field

  constructor(value) {
    this.#data = value;
  }

  show() {
    console.log(this.#data, this.#initializedData);
  }
}

let foo = new Foo(42);
foo.show();         // 42 43
```
## References
1. [JS OO Book > More Classes](https://launchschool.com/books/oo_javascript/read/more_classes)