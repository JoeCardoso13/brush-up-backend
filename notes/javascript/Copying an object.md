Created: 2024-08-22 11:47

When copying an [[Object]], it is **important** to know that if it is a **shallow copy**, it is going to duplicate [[Value]]s in memory only at 1 level. That means [[Mutability]] will still affect **nested** structures within. 

Let's see what happens at the first level:
```js
let arr = ['a', 'b', 'c'];
let copyOfArr = [...arr];

copyOfArr.push('d');

arr; // => [ 'a', 'b', 'c' ]
copyOfArr; // => [ 'a', 'b', 'c', 'd' ]
```
[[Mutability]] didn't affect both [[Object]]s at this level. However, the same can't be said about **nested structures** [[Mutability]]:
```js
let arr = [['a'], ['b'], ['c']];
let copyOfArr = arr.slice();

copyOfArr[1].push('d');

arr; // => [ [ 'a' ], [ 'b', 'd' ], [ 'c' ] ]
copyOfArr; // => [ [ 'a' ], [ 'b', 'd' ], [ 'c' ] ]
```
That's because even though we copied/duplicated the [[Object]] at 1 level, the deeper level [[Object]]s are still **shared**.

### Shallow copy
Here are 3 ways to create a **shallow** **copy** of an [[Object]]:
* Using the `slice` [[Method]] in an [[Array]].
* Using the [[Spread]] syntax in an [[Array]].
* Using `Object.assign` in an [[Object]] and passing `{}` as first argument.
### Deep copy
There is only 1 way to create a **deep** **copy** of an [[Object]]. Still, it is an **indirect** way and doesn't work if the [[Object]] has [[Method]]s and complex [[Object]]s like [[Date]]s or custom objects. It's using `JSON`:
```js
let arr = [{ b: 'foo' }, ['bar']];
let serializedArr = JSON.stringify(arr);
let deepCopiedArr = JSON.parse(serializedArr);
deepCopiedArr[1].push('baz');
deepCopiedArr; // => [ { b: 'foo' }, [ 'bar', 'baz' ] ]
arr; // => [ { b: 'foo' }, [ 'bar' ] ]
```
## References
1. [ courses > JS210 > lesson 5 ](https://launchschool.com/lessons/79b41804/assignments/40b5852e)