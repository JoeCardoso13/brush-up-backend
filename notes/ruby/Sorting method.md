Created: 2023-11-21 12:36

[[Return value]] will **always** be [[Array]]. 

Essentially these are built-in algorithms consisting of [[Spaceship operator]] usage, being carried out on all combinations of 2 elements from the [[Collection]] caller.

They are mostly performed on [[Array]]s. [[String]]s can't access them. [[Hash]]es have access since *Ruby 1.9 version* (because then they became ordered), when called without a block they're sorted by keys and always return an [[Array]]. The sorting [[Method]]s are provided by [[Enumerable module]] and, therefore, also available for [[Range]]s. 

There are 2 common sorting methods:
* [[Array.sort]]
* [[Array.sort_by]]

Less commonly used, there are these [[Hash]]es [[Sorting method]]s that operate like the ones above, by converting the [[Hash]] into [[Array]] under the hood:
* [[Hash.sort]]
* [[Hash.sort_by]]

[[Array]]s can have multiple types of [[Object]]s as its constituting elements. Therefore the outcome of [[Array.sort]] will depend on the specific implementations of [[Spaceship operator]] along with the inclusion of the [[Comparable module]] in the elements' [[Class]]. This is how the following classes employ the [[Spaceship operator]]:
* [[String comparison]]
* [[Symbol comparison]]
* [[Array comparison]]
* [[Integer comparison]]
* [[Float comparison]]
* [[Hash comparison]]
## References
1. [ courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)
2. [ RB101-RB119 Small Problems > Easy_5 > alphabetic numbers ](https://launchschool.com/exercises/c688f4e5)