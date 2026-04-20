Created: 2024-11-14 11:06

There are 3 ways to create objects:
* By assigning its [[Literal form]] to a [[Variable]].
* Using the [[new]] keyword on a [[Constructor function]].
* With the `Object.create` [[Object static method]].

---
Objects are "**compound**" [[Value]]s made up of [[Primitive]]s or other objects. Unlike [[Primitive]]s, objects can suffer [[Mutability]].

In general, a simple object in JS is a structure of association between key-[[Value]] pairs. In its [[Literal form]] it is defined through curly braces:
```javascript
let person = {
  name:    'Jane',
  age:     37,
  hobbies: ['photography', 'genealogy'], // trailing comma recommended
};
```
The **keys** are also referred to as **properties** and must have [[Type]] of [[String]] or symbol, whereas the [[Value]]s can be of any [[Type]] (including other, nested, objects). Properties can be accessed with bracket or dot notation:
```
> let obj = { a: 1, b: 2, c: 3 }
undefined
> obj['b']
2
> obj.b
2
```

When adding new pairs to the simple object, if using a [[Variable]] to reference the [[Value]] provided as **key** to key-[[Value]] pair, JavaScript uses [[Implicit type coercion]] to [[String]] on the [[Value]]:
```js
> let obj = {a: 1, b: 2, c: 3}
> let keyObj = {};
> obj[keyObj] = 13;
> obj
= { a: 1, b: 2, c: 3, '[object Object]': 13 }
```
---
There are a few different [[Object]] **creation** **patterns**:
* [[Object factory]]
* Using [[Class]] syntax
* [[Prototype pattern]] a.k.a [[Pseudo-classical pattern]]
* [[OLOO pattern]]
## References
1. [ Intro to JS > Objects ](https://launchschool.com/books/javascript/read/objects#whatareobjects)
2. [ OO JS book > Objects ](https://launchschool.com/books/oo_javascript/read/types_and_objects)