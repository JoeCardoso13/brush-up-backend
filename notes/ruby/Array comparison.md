Created: 2023-11-20 13:06

# `Array#<=>`

Moves from left to right using [[Spaceship operator]] on elements of the same index. As soon as the [[Return value]] is different from zero, it aborts the iteration and uses its result as the outcome of the [[Array]] comparison itself. If all evaluates to zero, then the outcome is based on the [[Array]]s length.

```ruby
[['a', 'cat', 'b', 'c'], ['b', 2], ['a', 'car', 'd', 3], ['a', 'car', 'd']].sort
# => [["a", "car", "d"], ["a", "car", "d", 3], ["a", "cat", "b", "c"], ["b", 2]]
```
## References
1. [courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)
2. [ Ruby Docs 3.2: array/Comparison](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-3C-3D-3E)