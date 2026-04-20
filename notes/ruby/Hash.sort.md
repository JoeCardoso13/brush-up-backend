Created: 2023-12-27 12:57

Comes from the [[Enumerable module]]. Effectively, it is the same as using [[Array.sort]] in the [[Array]] converted from the [[Hash]] with `Hash#to_a`.

[[Return value]] is **always** an [[Array]].

```ruby
{foo: 0, bar: 1, baz: 2}.sort # => [[:bar, 1], [:baz, 2], [:foo, 0]]
```
## References
1. [ Ruby Docs 3.2: Enumerable / sort ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-sort) 