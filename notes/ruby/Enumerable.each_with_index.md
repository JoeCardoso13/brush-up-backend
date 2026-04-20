Created: 2023-12-08 07:36

To iterate over the elements of a [[Collection]] and still have an index to work with, you don't need to call [[Integer.times]] or [[Integer.upto(Integer)]] while using [[Integer]] [[Method]]s, like `Integer#length`, to provide for the limits of [[Iteration]]. You can use `Enumerable#each_with_index` which is built to solve this problem:
```ruby
h = {}
%w[a b c d].each_with_index {|element, i| h[element] = i } # => ["a", "b", "c", "d"]
h # => {"a"=>0, "b"=>1, "c"=>2, "d"=>3}
```

Index always starts at zero. Its [[Return value]] is itself, just like the [[each Method]], it differs from [[Enumerable.each_with_object]] in this. If called without a [[Block]], returns an [[Enumerator]]. 
## References
1. [ Ruby Docs 3.2: Enumerable / each with index ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-each_with_index)