Created: 2024-01-18 10:15

## `#equal?`
Equivalent to `obj1 == obj2 && obj1.object_id == obj2.object_id`, which is equivalent to just comparing their [[Object ID]]s (latter [[Expression]]). 

Should not be defined for custom [[Class]]es.
## `#==` ([[Double equal]])
## `#===` ([[Tripple equal]])

## `#eql?`
The `#eql?` [[Method]] determines if two [[Object]]s contain the same **value** and if they're of the same [[Class]]. This [[Method]] is used most often by [[Hash]] to determine **equality** among its members.
## References
1. [ courses > RB120 > lesson 3 > 2. Equivalence ](https://launchschool.com/lessons/d2f05460/assignments/9cadd494)