Created: 2024-11-14 16:01

Are instance [[Method]]s that are private to an [[Object]]. These [[Method]]s can only be used within the [[Class]]. Otherwise, they look and act like ordinary [[Method]]s except that their names begin with a `#` and can't be called from outside the class:
```js
class MyClass {
  myPublic() {
    return this.#myPrivate();
  }

  #myPrivate() {
    return 'This is a private method';
  }
}

const instance = new MyClass();
console.log(instance.myPublic());  // This is a private method
console.log(instance.#myPrivate());
// Error: Private field '#myPrivate' must be declared in an
// enclosing class
```
## References
1. [JS OO Book > More Classes](https://launchschool.com/books/oo_javascript/read/more_classes)