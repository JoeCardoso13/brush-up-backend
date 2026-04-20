Created: 2024-09-14 18:18

Reduce calls the [[Callback function]] and passes as arguments each element of the [[Array]] caller. The [[Callback function]] may have 2 parameters, an **accumulator** and one that is assigned to **each** **element** of the [[Array]] caller (may also have an **index**). The [[Return value]] of each iteration of the [[Callback function]] call, i.e. every time the [[Function]] is called with (at least one) an [[Array]] element as argument, is assigned to the **accumulator** that keeps it throughout [[Function call]]s, i.e. between iterations.

Has following syntax:
```js
reduce(callbackFn)
reduce(callbackFn, initialValue)
```
`initialValue` is optional, if provided it is the starting value of the **accumulator**. If not, the **accumulator** starts with the first [[Array]] element [[Value]]. Note that providing the `initialValue` has the [[Callback function]] being called 1 more time than not providing it.

---
It is possible to re-create each [[Array]] processing function with reduce:
* `Array.prototype.some()`: to recreate this we start our **accumulator** to `false`. Then make the [[Callback function]] return a ternary [[Expression]] in which the **accumulator** is assigned to itself if it ever becomes `true`, otherwise it evaluates the current **element**: 
```js
let arr1 = [1, 2, 3, 4, 5]
let arr2 = [1, 'a', 2 ]
arr1.reduce((res, ele) => res ? res : ele > 4, false)
// true equivalent to arr1.some(ele => ele > 4)
arr1.reduce((res, ele) => res ? res : typeof ele === 'string', false)
// false equivalent to arr1.some(ele => typeof ele === 'string')
arr2.reduce((res, ele) => res ? res : typeof ele === 'string', false)
// true equivalent to arr2.some(ele => typeof ele === 'string')
```
* `Array.prototype.every()`: to recreate this we start our **accumulator** to `true`. Then make the [[Callback function]] return a ternary [[Expression]] in which the **accumulator** is assigned to itself if it ever becomes `false`, otherwise it evaluates the current **element**:
```js
let arr1 = [1, 2, 3, 4, 5]
let arr2 = [1, 'a', 2 ]
arr1.reduce((res, ele) => res ? typeof ele === 'number' : res, true)
// true equivalent to arr1.every(ele => typeof ele === 'number')
> arr2.reduce((res, ele) => res ? typeof ele === 'number' : res, true)
// false equivalent to arr2.every(ele => typeof ele === 'number')
```
* `Array.prototype.includes()`: to recreate this we start out **accumulator** to `false`. Then make the [[Callback function]] return a ternary [[Expression]] in which the **accumulator** is assigned to itself if it ever becomes `true`, otherwise it checks if the current **element** is the searched one:
```js
let arr1 = [1, 2, 3, 4, 13]
arr1.reduce((res, ele) => res ? res : ele === 13, false) // true
arr1.reduce((res, ele) => res ? res : ele === 12, false) // false
```
* `Math.max()` or `Math.min()`: to recreate this we start our **accumulator** to either `Infinity` or `-Infinity` if we are looking for the minimum or maximum, respectively. We simply compare each **element** with the **accumulator** and reassign it if the **element** is greater than, or less than the **accumulator** if we are looking for the maximum or minimum, respectively:
```js
let arr1 = [1, 2, 3, 4, 5]
> arr1.reduce((max, ele) => max > ele ? max : ele, -Infinity) // 5
> arr1.reduce((min, ele) => min < ele ? min : ele, Infinity) // 1
```
* `Array.prototype.filter()`: to recreate this we start our **accumulator** to an empty [[Array]]. Then we have our [[Callback function]] [[Push]] the **elements** we want to this [[Array]] and we make sure its [[Return value]] is the [[Array]]:
```js
let arr1 = [1, 2, 3, 4, 5]
arr1.reduce((arr, ele) => {
	if (ele > 2) arr.push(ele);
    return arr;
  }, []); // [ 3, 4, 5 ] equivalent to arr1.filter(ele => ele > 2)
```
* `Array.prototype.map()`: to recreate this we start our **accumulator** to an empty [[Array]]. Then we have our [[Callback function]] [[Push]] all the **elements** to this [[Array]] with the **transformation** we seek and we make sure its [[Return value]] is the [[Array]]:
```js
let arr1 = [1, 2, 3, 4, 5]
arr1.reduce((arr, ele) => {
	arr.push(String(ele));
	return arr;
  }, []) // [ '1', '2', '3', '4', '5' ] equivalent to arr1.map(String)
```
## References
1. [ courses > LS 215 > List Processing > Reducing ](https://launchschool.com/lessons/bfc761bc/assignments/32501eac)
2. [ MDN Docs > Arrays > Reduce ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)