Created: 2023-12-08 09:58

When no [[Block]] is given, returns a nested [[Array]] as if transposing the caller and argument [[Array]]s:
```ruby
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3]
c = [:c0, :c1, :c2, :c3]
d = a.zip(b, c)
d # => [[:a0, :b0, :c0], [:a1, :b1, :c1], [:a2, :b2, :c2], [:a3, :b3, :c3]]
```

When [[Block]] is used, calls it with each of the sub-[[Array]]s (formed as above) and returns `nil`:
```ruby
a = [:a0, :a1, :a2, :a3]
b = [:b0, :b1, :b2, :b3]
c = [:c0, :c1, :c2, :c3]
a.zip(b, c) {|sub_array| p sub_array} # => nil
```
Output:
```
[:a0, :b0, :c0]
[:a1, :b1, :c1]
[:a2, :b2, :c2]
[:a3, :b3, :c3]
```
## References
1. [ Ruby Docs 3.2: Array / zip ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-zip)