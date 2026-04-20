Created: 2024-08-20 09:12

Not recommended for [[Array]]s.

Iterates over the [[Object]] keys and, at each iteration, assigns the current key to the iterating [[Variable]] of choice:
```js
let person = {
  name: 'Bob',
  age: 30,
  height: '6 ft',
};

for (let prop in person) {
  console.log(person[prop]);
}                             // => Bob
                              //    30
                              //    6 ft
```
## References
1. [ Intro to JS > Objects ](https://launchschool.com/books/javascript/read/objects#whatareobjects)