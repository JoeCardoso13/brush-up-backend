Created: 2023-12-08 10:14

Its [[Return value]] is a [[Hash]] where:
* Each key is a [[Return value]] o the [[Block]].
* Each value is an [[Array]] of the elements for which the [[Block]] returned that key. 

```ruby
g = (1..6).group_by {|i| i%3 }
g # => {1=>[1, 4], 2=>[2, 5], 0=>[3, 6]}
h = {foo: 0, bar: 1, baz: 0, bat: 1}
g = h.group_by {|key, value| value }
g # => {0=>[[:foo, 0], [:baz, 0]], 1=>[[:bar, 1], [:bat, 1]]}
```

With no [[Block]] given returns [[Enumerator]].
## References
1. [ Ruby Docs 3.2: Enumerable / group by ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-group_by)