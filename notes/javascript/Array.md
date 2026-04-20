Created: 2024-08-19 09:58

It's an ordered list of elements. Its elements may have any [[Type]].

In JavaScript arrays are a special kind of [[Object]] (they are of [[Object]] [[Type]]). In its [[Literal form]] they are defined using square brackets:
```javascript
let myArray = [2, 'Pete', 2.99, 'another string']
```

JavaScript's built-in Array [[Method]]s (`join`, `forEach`, `push`, `splice`, etc.) take the [[Value]] of the `length` property into consideration while performing their operations. Some [[Method]]s just use the [[Value]], others set it, and some even do both.

#### Array Length
* Their **length** **property** is assignable. It can be reassigned as in [[Variable (re)assignment]]:
```js
let myArray = [1, 2, 3];
myArray.length; // returns 3

// setting to a larger value than the current largest array index
myArray.length = 5;
console.log(myArray); // logs (5) [1, 2, 3, empty × 2]
myArray.length; // returns 5

myArray[6] = "foo";
myArray.length; // returns 7
console.log(myArray); // logs (7) [1, 2, 3, empty × 3, "foo"]

// setting to a smaller value than the current largest array index with value
myArray.length = 2;
console.log(myArray); // logs [1, 2]

myArray.length = 5;
console.log(myArray); // logs (5) [1, 2, empty × 3]
myArray.length; // returns 5
```
- A property name is an array index when it is a non-negative integer. [[Value]]s that have been assigned to index properties are called **elements** of the array. All other property names and their associated [[Value]]s are **not** considered to be elements of the array.
- `Array.prototype.indexOf` returns `-1` if the value it is passed is not an element of the array, even if the value is associated with a non-index property.
- The [[Value]] of `length` is **entirely** **dependent** on the largest array index.
- Logging an array logs all the indexed values and every `key: value` pair that the object contains. It logs only the value (e.g., `'baz'`, `'qux'`) if it's an element. Otherwise, it logs the `key: value` pair (e.g., `foo: 'bar'`) if it isn't an element (see line 18).
- To count all of the properties in an Array object, use `Object.keys(array).length` (see line 19). Don't use `array.length`.

---
Here are some peculiarities of arrays in JS due to the fact mentioned above:

* It can have empty places (although they'll return [[Undefined]] if requested, it would be **incorrect** to claim they're [[Undefined]], they're simply not set): 
```
> let arr = [1, 2, 3]
> arr.length = 6
> arr
[ 1, 2, 3, <3 empty items> ]
```
* Indexes are just a special [[Object]] property:
```
> Object.keys(arr)
[ '0', '1', '2' ]
```
* Key-[[Value]] pairs can be added at will, although, if outside the boundaries of indexes, they won't count towards length. 
```
> arr = [1, 2, 3]
= [ 1, 2, 3 ]

> arr[-3] = 4
= 4

> arr
= [ 1, 2, 3, '-3': 4 ]

> arr[3.1415] = 'pi'
= 'pi'

> arr["cat"] = 'Fluffy'
= 'Fluffy'

> arr
= [ 1, 2, 3, '-3': 4, '3.1415': 'pi', cat: 'Fluffy' ]

> arr.length
= 3

> Object.keys(arr)
= [ '0', '1', '2', '-3', '3.1415', 'cat' ]
```
* Since arrays are not good for [[Strict equality]] [[Comparison]], we can create a [[Function]] for that, and/or transform into [[String]] then compare.
* Be careful with the last point:
```
> let inner = [3, 4];
> let a = [1, 2, inner, 5]

> a.includes([3, 4])
= false

> a.includes(inner)
= true

> let inner = [3, 4];
> let a = [1, 2, inner, 5]

> a.indexOf([3, 4])
= -1

> a.indexOf(inner)
2
```

Given that [[Array]] is an [[Object]] it follows their general guidelines for [[Implicit type coercion]]. For sums (`+`) JavaScript converts to [[String]]:
```
let initials = ['A', 'H', 'E'];
initials + 'B';                   // "A,H,EB"
initials;                         // [ "A", "H", "E" ]
initials + ['B'];      // "A,H,EB"
initials;              // [ "A", "H", "E" ]
```
For other **arithmetic operations** it tries to convert them to [[Number]]s:
```
[1] * 2;              // 2 -- becomes '1' * 2, then 1 * 2
[1, 2] * 2;           // NaN -- becomes '1,2' * 2, then NaN * 2
[5] - 2;              // 3
[5] - [2];            // 3
5 - [2];              // 3
5 - [2, 3];           // NaN -- becomes 5 - '2,3', then 5 - NaN
[] + [];              // '' -- becomes '' + ''
[] - [];              // 0 -- becomes '' - '', then 0 - 0
+[];                  // 0
-[];                  // -0
```
With [[Loose equality]] it implicitly coerces to [[String]]:
```
[] == '0';               // false -- becomes '' == '0'
[] == 0;                 // true -- becomes '' == 0, then 0 == 0
[] == false;             // true -- becomes '' == false, then 0 == 0
[] == ![];               // true -- same as above
[null] == '';            // true -- becomes '' == ''
[undefined] == false;    // true -- becomes '' == false, then 0 == 0
[false] == false;        // false -- becomes 'false' == 0, then NaN == 0
```
Use `Array.isArray(value)` to check if the [[Value]] is an array or not.
## References
1. [ Intro to JS > Arrays ](https://launchschool.com/books/javascript/read/arrays#whatisanarray)