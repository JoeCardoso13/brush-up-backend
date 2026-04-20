Created: 2023-11-03 10:54

[[Hash]]es have built-in comparison methods that actually check for sub-sets, e.g.:
```ruby
h1 = {foo: 0, bar: 1}
h2 = {foo: 0, bar: 1, baz: 2}
h1 < h2 # => true
h2 < h1 # => false
h1 < h1 # => false
h1 <= h1 # => true
```

[[Hash]]es do not have a [[Spaceship operator]], so cannot be compared in an ordering sense.
## References
1. [Ruby Docs 3.2: hashes/Comparison](https://docs.ruby-lang.org/en/3.2/Hash.html#method-i-3C)