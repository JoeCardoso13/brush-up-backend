Created: 2024-01-18 12:41

Below is a table that shows which operators are real operators, and which are [[Method]]s disguised as operators (listed by order of [[Precedence]]; highest first):

| Method | Operator                                                                               | Description                                                                         |
| ------ | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| no     | `.`, `::`                                                                              | Method/constant resolution operators                                                |
| yes    | `[]`, `[]=`                                                                            | Collection element getter and setter.                                               |
| yes    | `**`                                                                                   | Exponential operator                                                                |
| yes    | `!`, `~`, `+`, `-`                                                                     | Not, complement, unary plus and minus (method names for the last two are +@ and -@) |
| yes    | `*`, `/`, `%`                                                                          | Multiply, divide, and modulo                                                        |
| yes    | `+`, `-`                                                                               | Plus, minus                                                                         |
| yes    | `>>`, `<<`                                                                             | Right and left shift                                                                |
| yes    | `&`                                                                                    | Bitwise "and"                                                                       |
| yes    | `^`, `\|`                                                                              | Bitwise exclusive "or" and regular "or" (inclusive "or")                            |
| yes    | `<=`, `<`, `>`, `>=`                                                                   | Less than/equal to, less than, greater than, greater than/equal to                  |
| yes    | `<=>`, `==`, `===`, `!=`, `=~`, `!~`                                                   | Equality and pattern matching (`!~` cannot be directly defined)                     |
| no     | `&&`                                                                                   | Logical "and"                                                                       |
| no     | `\|`                                                                                   | Logical "or"                                                                        |
| no     | `..`, `...`                                                                            | Inclusive range, exclusive range                                                    |
| no     | `? :`                                                                                  | Ternary if-then-else                                                                |
| no     | `=`, `%=`, `/=`, `-=`, `+=`, `\|=`, `&=`, `>>=`, `<<=`, `*=`, `&&=`, `\|=`, `**=`, `{` | Assignment (and shortcuts) and block delimiter                                      |
## References
1. [ courses > RB120 > lesson 3 > Fake Operators ](https://launchschool.com/lessons/d2f05460/assignments/9a7db2ee)