Created: 2023-12-27 16:10

Only present in the [[Enumerable module]].

This is effectively a shortcut for using [[Array.sort_by]] (or [[Hash.sort_by]]) and then picking first place. Analogously, [[min]] relates to [[Array.sort]] (or [[Hash.sort]]). Using an [[Integer]] argument into an [[Array]] of mins.

```ruby
(1..4).min_by {|element| -element }                    # => 4
%w[a b c d].min_by {|element| -element.ord }           # => "d"
{foo: 0, bar: 1, baz: 2}.min_by {|key, value| -value } # => [:baz, 2]

(1..4).min_by(2) {|element| -element }
# => [4, 3]
%w[a b c d].min_by(2) {|element| -element.ord }
# => ["d", "c"]
{foo: 0, bar: 1, baz: 2}.min_by(2) {|key, value| -value }
# => [[:baz, 2], [:bar, 1]]
```
## References
1. [ courses > RB119 > Study Guide for RB119 interview > video 1 ](https://launchschool.com/lessons/a999a6a0/assignments/4d3af2d8)
2. [ Ruby Docs 3.2: Enumerable / min_by ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-min_by)