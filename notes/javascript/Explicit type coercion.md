Created: 2024-08-20 10:46

Sometimes we need [[Method]]s to coerce [[String]] to [[Number]]:
* `Number(str)` or `+(str)`
* `ParseInt(str, radix=10)`
* `ParseFloat(str)`
Or [[Number]] to [[String]]:
* `String(num)`
* `num.toString()`
* `123 + ''` or `'' + 123` (using implicit [[Type]] coercion)
These also work with other data [[Type]]s such as [[Boolean]] or [[Array]]s, just are more commonly used as above.
## References
1. [ JS210 > lesson 1 > JS Basics ](https://launchschool.com/lessons/7377ece4/assignments/3d2e392a)