Created: 2024-11-14 10:43

JavaScript is **not** a traditional OO language. Technically, it doesn't support classes in the conventional sense. Even though it has something it calls classes, those classes are merely **syntactical** **sugar** for JavaScript's [[Type]] system. The class syntax makes it easier to use and understand OO in JavaScript programs, especially for developers learning JavaScript after working with traditional [[Object Oriented]] languages.

Again, to emphasize: the class syntax does not introduce a new [[Object Oriented]] [[Inheritance]] model to JavaScript. Instead, it simply provides some **syntactic** **sugar** on top of the [[Prototypal inheritance]] system.

Example:
```js
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }

  area() {
    return this.height * this.width;
  }
}

const myRectangle = new Rectangle(10, 5);
console.log(myRectangle.area());        // 50

class Square extends Rectangle {
  constructor(side) {
    super(side, side);
    this.side = side;
  }
}

const mySquare = new Square(6);
console.log(mySquare.area());           // 36
console.log(mySquare.side);             // 6

console.log(myRectangle); // Rectangle { height: 10, width: 5 }
console.log(mySquare);    // Square { height: 6, width: 6, side: 6 }

console.log(mySquare instanceof Square);          // true
console.log(mySquare instanceof Rectangle);       // true

console.log(myRectangle instanceof Square);       // false
console.log(myRectangle instanceof Rectangle);    // true
```
---
In adding **syntactic sugar** on top of the [[Prototypal inheritance]] system to simulate traditional [[Object Oriented]] languages, JavaScript has recently added:
* [[Private field]]s 
* [[Private method]]s
* [[Getter]]s and [[Setter]]s
* [[Static field-property]]s
* [[Static method]]s
## References
1. [ OO JS book > Objects ](https://launchschool.com/books/oo_javascript/read/types_and_objects)