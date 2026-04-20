Created: 2023-10-18 14:59

If no argument is given, it removes and returns the last argument:
```ruby
a = [:foo, 'bar', 2]
a.pop # => 2
a # => [:foo, "bar"]
```
When positive Integer argument `n` is given, removes the last `n` elements; returns those elements in a new Array.
## References
1. [Ruby Docs 3.2: array/Pop](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-pop)