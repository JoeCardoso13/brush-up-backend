Created: 2024-08-21 11:40

We can be more precise in describing how JavaScript resolves a [[Variable]] to a [[Value]] by checking through the hierarchy of [[Variable scope]]s containing the [[Variable]]. We can use the concept of closure. Take the following code , for example:
```js
var qux = 2;
function foo() {
  var qux = 1;
  bar();
}

function bar() {
  console.log(qux);
}

foo();  // logs 2
```
The simple concept of walking through the hierarchy of [[Variable scope]]s, from **local** to **global** is not enough to understand how JavaScript disambiguates which `quix`  [[Variable]] to resolve to.

Every [[Function definition]] creates inside JavaScript a sort of "map" pointing to all [[Variable]]s it needs to run. This "map" is the [[Function]]'s closure. Because it happens at the **creation phase**, that is before JavaScript **executes** the code, the closure encloses the [[Variable]]s lexically available to the [[Function definition]], **not** its [[Function call]] (!!!). This explains how JavaScript disambiguates the `quix` [[Variable]] in the previous example. This is also referred to as [[Lexical scoping]].

This comes into play when we use [[Function]]s returned by another [[Function call]]: 
```js
> function makeCounter() {
	let count = 0;
	
	return function() {
		count += 1;
		return count;
	}
}
> counter1 = makeCounter();
> counter2 = makeCounter();
> counter1()
= 1
> counter1()
= 2
> counter1()
= 3
> counter2()
= 1
> counter2()
= 2
```
The [[Anonymous function]] that is the [[Return value]] of `makeCounter` [[Function call]], has a **local** [[Variable]] `count` in its closure. By producing 2 different [[Anonymous function]]s, each with a **local** `count` in its closure, we create 2 parallel, independent counters.

This concept is important to understand [[Partial function]]s and [[Garbage collection]].
## References
1. [ courses > JS210 > lesson 2 > Functions and Variable Scope ](https://launchschool.com/lessons/7cd4abf4/assignments/0ea7c745)