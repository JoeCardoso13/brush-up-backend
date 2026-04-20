Created: 2023-10-19 13:51

## `Hash#[]=`

Without [[Ruby's syntactical sugar]]:
```ruby
hsh = { a: 1, b: 2, c: 3 }
hsh.[]=(:b, 4)
hsh # => {:a=>1, :b=>4, :c=>3}
```

It associates the given *value* with the given *key*. If given *key* exists, replaces its *value* with given *value*. If given *key* does not exist, adds the *key* *value* pair (new entry is last in order).
## References
1. [Ruby Docs 3.2: Hash](https://docs.ruby-lang.org/en/3.2/Hash.html#method-i-5B-5D-3D)