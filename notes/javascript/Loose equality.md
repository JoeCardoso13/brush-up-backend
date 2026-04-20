Created: 2024-08-19 18:10

`==`

Should be avoided. It is similar to [[Strict equality]] but when the [[Type]] of the operands is different, it tries to coerce them before comparing. It may coerce both of them in some cases. This can lead to unexpected results. Some rules for its [[Implicit type coercion]] are as follows:

When one *operand* is a [[String]] and the other is a [[Number]], the [[String]] is converted to a [[Number]]:
```
'42' == 42            // true
42 == '42'            // true
42 == 'a'             // false -- becomes 42 == NaN
0 == ''               // true -- becomes 0 == 0
0 == '\n'             // true -- becomes 0 == 0
```

When one operand is a [[Boolean]], it is converted to a [[Number]]:
```
42 == true            // false -- becomes 42 == 1
0 == false            // true -- becomes 0 == 0
'0' == false          // true -- becomes '0' == 0, then 0 == 0 (two conversions)
'' == false           // true -- becomes '' == 0, then 0 == 0
true == '1'           // true
true == 'true'        // false -- becomes 1 == 'true', then 1 == NaN
```

When one operand is [[Null]] and the other is [[Undefined]], the non-strict *operator* always returns `true`. If both *operands* are [[Null]] or both are [[Undefined]], the return value is `true`. Comparing [[Null]] or [[Undefined]] to all other [[Value]]s returns `false`:
```
null == undefined      // true
undefined == null      // true
null == null           // true
undefined == undefined // true
undefined == false     // false
null == false          // false
undefined == ''        // false
undefined === null     // false -- strict comparison
```

When one of the operands is [[NaN]], the [[Comparison]] always returns `false`:
```
NaN == 0              // false
NaN == NaN            // false
NaN === NaN           // false -- even with the strict operator
NaN != NaN            // true -- NaN is the only JavaScript value not equal to itself
```
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)