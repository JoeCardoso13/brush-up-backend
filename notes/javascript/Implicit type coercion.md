Created: 2024-08-19 10:54

It's when JS automatically does [[Explicit type coercion]].

* For sums (`+`), when both *operands* are a combination of [[Number]]s, [[Boolean]]s, [[Null]]s, or [[Undefined]], they are converted to numbers and added together:
```
1 + true        // 2
1 + false       // 1
true + false    // 1
null + false    // 0
null + null     // 0
1 + undefined   // NaN
```
When one of the *operands* is an [[Object]] (including [[Array]]s and [[Function]]s), both *operands* are converted to [[String]] and concatenated together:
```
[1] + 2                     // "12"
[1] + '2'                   // "12"
[1, 2] + 3                  // "1,23"
[] + 5                      // "5"
[] + true                   // "true"
42 + {}                     // "42[object Object]"
(function foo() {}) + 42    // "function foo() {}42"
```

* For the other **arithmetic** *operators*, `-`, `*`, `/`, `%`, are only defined for [[Number]]s, so JavaScript converts both *operands* to [[Number]]s:
```
1 - true                // 0
'123' * 3               // 369 -- the string is coerced to a number
'8' - '1'               // 7
-'42'                   // -42
null - 42               // -42
false / true            // 0
true / false            // Infinity
'5' % 2                 // 1
```

* [[Loose equality]] *operators* have their own rules for implicit [[Type]] coercion. 

* When accessing or creating a [[Value]] from an [[Object]]'s property through square bracket notation, if we don't provide a [[String]] as key/property JavaScript coerces the [[Value]] provided to a [[String]].
## References
1. [ Intro to JS > Basics ](https://launchschool.com/books/javascript/read/basics#datatypes)
2. [ JS210 > lesson 1 > JS Basics ](https://launchschool.com/lessons/7377ece4/assignments/3d2e392a)