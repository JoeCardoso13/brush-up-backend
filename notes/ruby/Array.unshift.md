Created: 2023-10-18 15:00

=> Alias for `Array#prepend`
Will prepend arguments to beginning of [[Array]] (returns `self`):
```ruby
a = [:foo, 'bar', 2]
a.unshift(:bam, :bat) # => [:bam, :bat, :foo, "bar", 2]
```
## References
1. [Ruby Docs 3.2: array/Unshift](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-unshift)