Created: 2024-08-21 12:04

A **Partial** **Function** **Application** is when we use JavaScript's feature of having [[Function]]s as 1st class [[Object]]s to nest [[Function]]s in a way that allows us to incrementally provide all arguments needed for a certain [[Function call]].

We call a Partial Function Application a [[Function]] that takes an argument and uses it to partially fill the parameters of its returned [[Function]]. Example:
```js
function add(first, second) {
  return first + second;
}

function makeAdder(firstNumber) {
  return function(secondNumber) {
    return add(firstNumber, secondNumber);
  };
}

let addFive = makeAdder(5);
let addTen = makeAdder(10);

console.log(addFive(3));  // 8
console.log(addFive(55)); // 60
console.log(addTen(3));   // 13
console.log(addTen(55));  // 65
```
Remember, in **partial function applications** we have 3 [[Function]]s:
1) The primary, i.e. the one that gets all parameters and returns a meaningful [[Value]].
2) The maker/factory, i.e. the one that produces partially filled [[Function]]s.
3) The deliverer/carrier/intermediary, i.e. the one used solely as a channel to pass on the partially filled primary without actually invoking it. 
---
They are handy when handling **asynchronous** calls:
```js
function speak(string) {
  console.log(string);
}

var delayedFunction = function(fn) {
  return function(val, delay) {
    setTimeout(function() {
      fn(val);
    }, delay);
  };
};

var delayedSpeak = delayedFunction(speak);
delayedSpeak("I'm late!", 1000);      // logs "I'm late" after a 1 second delay
```
## References
1. [ courses > JS210 > lesson 2 > Functions and Variable Scope ](https://launchschool.com/lessons/7cd4abf4/assignments/0ea7c745)