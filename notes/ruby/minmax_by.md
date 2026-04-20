Created: 2023-12-27 17:00

Just like [[min_by]] and [[max_by]] put together, but it doesn't accept [[Integer]] argument.

```ruby
(1..4).minmax_by {|element| -element }
# => [4, 1]
%w[a b c d].minmax_by {|element| -element.ord }
# => ["d", "a"]
{foo: 0, bar: 1, baz: 2}.minmax_by {|key, value| -value }
# => [[:baz, 2], [:foo, 0]]
[].minmax_by {|element| -element }
# => [nil, nil]
```
## References
1. [ Ruby Docs 3.2: Enumerable / minmax_by ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-minmax_by)