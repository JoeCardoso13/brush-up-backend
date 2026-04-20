Created: 2024-08-19 18:13

`>` or `>=` (greater or equal than)

Returns `true` when the left side operand's [[Value]] is greater (or equal if so) than the right hand side one. They are defined for [[Number]]s (numeric [[Comparison]]) and [[String]]s (lexicographic order). There are no strict versions of these *operators*. When both operands are [[String]]s, JavaScript compares them lexicographically. Otherwise, JavaScript converts both *operands* to [[Number]]s before comparing them:
```
11 > '9'              // true -- '9' is coerced to 9
'11' > 9              // true -- '11' is coerced to 11
123 > 'a'             // false -- 'a' is coerced to NaN; any comparison with NaN is false
123 <= 'a'            // also false
true > null           // true -- becomes 1 > 0
true > false          // true -- also becomes 1 > 0
null <= false         // true -- becomes 0 <= 0
undefined >= 1        // false -- becomes NaN >= 1
```

[[String]] [[Comparison]] (lexicographic order) moves from left to right comparing character by character (using their ASCII code) until reaching a result different from a tie. In case it reaches the end of an operand before that, it evaluates per length.

Do **not** try to use with [[Object]]s.
## References
1. [ Intro to JS > Flow Control ](https://launchschool.com/books/javascript/read/flow_control)