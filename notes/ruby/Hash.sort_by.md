Created: 2023-11-21 15:14

Comes from the [[Enumerable module]]. Effectively, it is the same as using [[Array.sort_by]] in the [[Array]] converted from the [[Hash]] with `Hash#to_a`.

[[Return value]] is **always** an [[Array]].

When calling `sort_by` on a [[Hash]], either two arguments are passed to the [[Block]], or one argument that becomes an array with the key-value pair.

```ruby
people = { Kate: 27, john: 25, Mike:  18 }
people.sort_by do |_, age|
  age
end
# => [[:Mike, 18], [:john, 25], [:Kate, 27]]

h = {foo: 2, bar: 1, baz: 0}
h.sort_by{|key, value| value } # => [[:baz, 0], [:bar, 1], [:foo, 2]]
h.sort_by{|key, value| key }   # => [[:bar, 1], [:baz, 0], [:foo, 2]]
```
## References
1. [courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)
2. [ Ruby Docs 3.2: Enumerable / sort_by ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-sort_by)