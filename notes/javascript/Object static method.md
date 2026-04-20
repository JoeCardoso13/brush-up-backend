Created: 2024-11-14 11:09

Some useful [[Static method]]s of the [[Object]] [[Constructor function]] for converting from its [[Literal form]] to [[Array]] [[Type]] are `Object.keys(obj)`, `Object.values(obj)` and `Object.entries(obj)`:
```
> Object.keys(obj)
[ 'a', 'b', 'c' ]
> Object.values(obj)
[ 1, 2, 3 ]
> Object.entries(obj)
[ [ 'a', 1 ], [ 'b', 2 ], [ 'c', 3 ] ]

```

We can use `Object.is(value1, value2)` to find equality where [[Strict equality]] fails :
```
> let value = -0;
> Object.is(value, 0)
= false
> Object.is(value, -0)
= true
```

You can use `Object.assign({},obj1,obj2)` to create a **new** **object** out of the union of how many objects you want (if only 1, then you're [[Copying an object]]), or you can mutate an object to unite it with how many objects you want `Object.assign(obj1,obj2)`.

`Object.create(obj)` is a way to [[Create object]] that is empty and has `obj` as its [[Object prototype]].

`Object.getPrototypeOf(obj)` and `Object.setPrototypeOf(obj1, obj2)` are ways to retrieve and set, respectively, the [[Object prototype]] of an [[Object]]. It is **not** recommended to use it to **set** the [[Object prototype]] though, due to **performance** issues.

Combining 2 of the previous [[Static method]]s we have a powerful and simple way to extend JavaScript's built-in [[Constructor function]]s:
```js
NewArray.prototype = Object.create(Object.getPrototypeOf([]));
NewArray.prototype.first = function() {
  return this[0];
};
let newArr = new NewArray();
let oldArr = new Array();

oldArr.push(5);
newArr.push(2);
console.log(newArr.first());           // => 5
console.log(oldArr.first);             // => undefined
```

`Object.getOwnPropertyNames` are ways to disambiguate behavior delegated to the [[Prototype chain]] to the [[Object]]'s own [[Method]]s.

`Object.defineProperties` allows you to set unwritable properties on an [[Object]]:
```js
let obj = {
  name: 'Obj',
};

Object.defineProperties(obj, {
  age: {
    value: 30,
    writable: false,
  },
});

console.log(obj.age); // => 30
obj.age = 32;         // throws an error in strict mode
console.log(obj.age); // => 30
```

`Object.freeze` makes properties unable to be reassigned ([[Variable (re)assignment]]). Once frozen an [[Object]] cannot be unfrozen.

---
???
To delete a **pair** you use the `delete` keyword:
```
> delete person['gender']
= true
```
`instanceof`, `typeof` keywords???

## References
1. [ Intro to JS > Objects ](https://launchschool.com/books/javascript/read/objects#whatareobjects)