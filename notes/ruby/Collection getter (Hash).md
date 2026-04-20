Created: 2023-10-21 23:49

## `Hash#[]`

Without [[Ruby's syntactical sugar]]:
```ruby
hsh = { a: 1, b: 2, c: 3 }
hsh.[](:b) # => 2
```

It returns a **reference** to existing [[Object]] (if found), does **not** create new [[Object]] (thence [[Object passing]] may take place). **Different** from [[Collection getter (String)]] in this regard.

It returns the value associated with given key, if found. If key is not found, [[Return value]] is **default**. **Default** can be retrieved and set with `Hash#default` and `Hash#default=` respectively: 
```
h = {a: 1, b: 2}
h.default
=> nil
h.default= 13
h[:c]
=> 13
```
Can also be set when creating the [[Hash]] by using the syntax:
```
hsh = Hash.new('default_value')
hsh.default
=> 'default_value'
```
Using `Hash#fetch` instead of hash keyed to retrieve values avoids the **default** bringing an [[Exception]] when key is not found.
## References
1. [Ruby Docs 3.2: hash/](https://docs.ruby-lang.org/en/3.2/Hash.html#method-i-5B-5D)
2. [Ruby Docs 3.2: hash/default_value](https://docs.ruby-lang.org/en/3.2/Hash.html#class-Hash-label-Default+Values)