Created: 2023-10-04 11:48

A "truthy" value is any value that when evaluated in [[Conditional expression]] will follow the same path as their corresponding [[Boolean]] value: `true`.

**All** Ruby values are "truthy", except:
* `nil`
* `false`

Therefore, the following values are "truthy" in Ruby, and will follow the same path as the `true` [[Boolean]] in [[Control Expression]]:
* `''`
* `0`
* `0.0`
* `{}`
* `[]`

Note that an expression that Ruby _considers true_ is **not** the same as **the** `true` [[Object]].

Using the [[BasicObject]]'s' method `!` twice returns the [[Boolean]] equivalent for "truthy", i.e. `true`.
## References
1. [courses > RB101 > lesson 2 > 5. Truthiness](https://launchschool.com/lessons/8a39abff/assignments/f72b8e01)