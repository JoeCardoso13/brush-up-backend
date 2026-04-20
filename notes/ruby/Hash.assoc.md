Created: 2023-10-24 13:36

If the given argument key is found, returns a 2-element [[Array]] containing that key and its corresponding value:
```ruby
h = {foo: 0, bar: 1, baz: 2}
h.assoc(:bar) # => [:bar, 1]
```
Returns `nil` if key key is not found.
## References
1. [Ruby Docs 3.2: hash/assoc](https://docs.ruby-lang.org/en/3.2/Hash.html#method-i-assoc)