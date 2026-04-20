Created: 2023-10-24 13:15

With no argument, a `nil` argument, or with negative argument `level`, flattens all levels:
```ruby
a = [ 0, [ 1, [2, 3], 4 ], 5 ]
a.flatten! # => [0, 1, 2, 3, 4, 5]
[0, 1, 2].flatten! # => nil
a = [ 0, [ 1, [2, 3], 4 ], 5 ]
a.flatten!(-1) # => [0, 1, 2, 3, 4, 5]
a = [ 0, [ 1, [2, 3], 4 ], 5 ]
a.flatten!(-2) # => [0, 1, 2, 3, 4, 5]
[0, 1, 2].flatten!(-1) # => nil
```
With non-negative [[Integer]] argument, flattens recursively through levels:
```ruby
a = [ 0, [ 1, [2, 3], 4 ], 5 ]
a.flatten!(1) # => [0, 1, [2, 3], 4, 5]
a = [ 0, [ 1, [2, 3], 4 ], 5 ]
a.flatten!(2) # => [0, 1, 2, 3, 4, 5]
a = [ 0, [ 1, [2, 3], 4 ], 5 ]
a.flatten!(3) # => [0, 1, 2, 3, 4, 5]
[0, 1, 2].flatten!(1) # => nil
```

Returns `nil` if no change is made.
## References
1. [Ruby Docs 3.2: array/Flatten!](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-flatten-21)