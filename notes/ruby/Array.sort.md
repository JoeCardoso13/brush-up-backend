Created: 2023-11-21 14:44

How this [[Sorting method]] will order the elements in the [[Array]] will depend on the specific type of elements. Furthermore, it will depend on how that specific type of element defines the [[Spaceship operator]] usage.

When called with no [[Block]], it simply applies the [[Spaceship operator]] on all combinations of elements from the [[Array]] caller. We can also call `sort` with a [[Block]]. The [[Block]] needs two arguments passed to it (the two items to be compared) and the [[Return value]] of the [[Block]] has to be `-1`, `0`, `1` or `nil`.

---

The complexity of this [[Method]] easily builds up when applied to nested [[Array]]s. Because of the [[Array comparison]] (i.e. its [[Spaceship operator]] usage) procedural definition, it is going to keep stepping down the chain of nested [[Array]]s until it finds another, different type of [[Object]] (e.g. [[String]]). Then it will apply the [[Spaceship operator]] to compare that [[Object]] (e.g. [[String comparison]]) and determine the position of the elements in the [[Array]]. The following example illustrates it:
```ruby
arr = [['1', '8', '11'], ['2', '6', '13'], ['2', '12', '15'], ['1', '8', '9']]

arr.sort # => [["1", "8", "11"], ["1", "8", "9"], ["2", "12", "15"], ["2", "6", "13"]]

arr.sort_by do |sub_arr|
  sub_arr.map(&:to_i)
end
# => [["1", "8", "9"], ["1", "8", "11"], ["2", "6", "13"], ["2", "12", "15"]]
```
## References
1. [ courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)
2. [ courses > RB110 > lesson 2 > 4. Working with Blocks ](https://launchschool.com/lessons/fa1f5e7e/assignments/084fe222)