Created: 2023-11-21 14:56

*'Usually'* called with a [[Block]] (or it returns [[Enumerator]]). The code in the [[Block]] determines the criterion for ordering. 
```ruby
['cot', 'bed', 'mat'].sort_by do |word|
  word[1]
end
# => ["mat", "bed", "cot"]
```
When the [[Block]] is filled by a single [[Object]]:
	The requisite is that each element given to the [[Block]] on each [[Iteration]] has a uniquely, bi-directional relationship with the single [[Object]] filling the [[Block]]. The default sorting criterion will apply to the [[Collection]] formed by these [[Object]]s and then transmitted to the [[Array]] caller.

Interestingly, [[Array]] defines a `#sort_by!` method; `Array#sort_by!` is not provided by `Enumerable`, so `#sort_by!` may not be available for other collections.

The [[Return value]] is **always** an [[Array]].
## References
1. [ courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)
2. [ Ruby Docs 3.2: Enumerable Module](https://docs.ruby-lang.org/en/3.2/Enumerable.html)