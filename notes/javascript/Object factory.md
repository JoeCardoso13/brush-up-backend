Created: 2024-11-14 14:58

An **object** **factory** is simply a [[Function]] that returns a new [[Object]]. In JavaScript, **object factories** let you create multiple instances of similar [[Object]]s without defining a specific [[Type]].

Example:
```js
function createCat(name, color, age) {
  return {
    name,
    color,
    age,

    speak() {
      console.log(
        `Meow. I am ${this.name}. ` +
        `I am a ${this.age}-year-old ${this.color} cat.`
      );
    }
  };
}
```

As a pattern to [[Create object]]s, it offers a few advantages:
* [[Object]]s created are highly customizable based on the arguments passed to the [[Function call]]. 
* It's more straightforward/simple in comparison to other patterns because it doesn't handle [[Prototypal inheritance]].
* It simplifies the use of [[this]] keyword.
* Can use [[Closure]] to create [[Private data]].

And disadvantages:
* Each [[Object]] gets its own copy of [[Method]]s. It makes it less efficient than other patters where [[Inheritance]] takes care of that and each [[Object]] gets only a pointer.
* [[Object]]s created don't have a [[Type]]:
```js
function Foo() {
  return {
    foo: 42,
  };
}

let obj = Foo();
console.log(obj instanceof Foo); // false
console.log(obj.constructor);    // [Function: Object]
```
## References
1. [ OO JS Book > Object Factories ](https://launchschool.com/books/oo_javascript/read/object_factories)