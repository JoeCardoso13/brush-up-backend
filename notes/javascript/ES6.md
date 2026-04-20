Created: 2024-08-22 10:15

[Here you find a comprehensive list of the syntactic sugar implemented in JavaScript from ES6.](https://launchschool.com/gists/2edcf7d7)

From 2015, it introduced:
* [[Class]] syntax.
* **compact method syntax**. Rather than writing the property name, a colon, and then a function expression, you can use a much simplified syntax:
```js
let myObj = {
  foo: function (who) {
    console.log(`hello ${who}`);
  },

  bar: function (x, y) {
    return x + y;
  },
};
// can be compacted into:
let myObj = {
  foo(who) {
    console.log(`hello ${who}`);
  },

  bar(x, y) {
    return x + y;
  },
};
```
* **concise property initializers**. When using simply a **name** and a comma instead of a key-[[Value]] pair for declaring an [[Object]] in its [[Literal form]], JavaScript will look for a [[Variable]] with the same **name** and, if it finds, uses it like so:
```js
function xyzzy(foo, bar, qux) {
  return {
    foo, // like foo: foo,
    bar, // like bar: bar,
    answer: qux,
  };
}
```
* [[Array]] and [[Object]] **de-structuring**. When initializing [[Variable]]s from an [[Object]] or [[Array]], we can do like so:
```js
let obj = {
  foo: "foo",
  bar: "bar",
  qux: 42,
};
let { foo, bar, qux } = obj;

let bar = [1, 2, 3, 4, 5, 6, 7];
let [ first, , , fourth, fifth, , seventh ] = bar; // can skip
```
Be **careful** if it's [[Variable (re)assignment]], JavaScript needs parenthesis to know it's not a [[Block]]:
```js
({ foo, bar, qux } = obj);
```
A notably frequent use case for [[Array]]s is swapping [[Value]]s:
```js
let one = 1;
let two = 2;

[ one, two ] =  [two, one];
```
* `let` and `const` [[Variable declaration]]s.
* [[Arrow function]]s.
* [[Spread]] syntax.
* [[Rest]] syntax.
## References
1. [ courses > JS210 > lesson 5 > Intro ](https://launchschool.com/lessons/79b41804/assignments/091246c3)