Created: 2023-10-18 14:59

=> Alias for `Array#append`.
Will append potentially **multiple** arguments to **end** of [[Array]] (returns `self`):
```ruby
a = [:foo, 'bar', 2]
a.push(:baz, :bat) # => [:foo, "bar", 2, :baz, :bat]
```

Similar to [[Array.shovel]] however the latter only takes **1 argument**. 

Similar to [[Array.concat]] however the latter automatically **flattens** the returned [[Array]] ('self').
## References
1. [Ruby Docs 3.2: array/Push](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-push)