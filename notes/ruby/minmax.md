Created: 2023-12-27 16:57

Just like [[min]] and [[max]] put together, but it doesn't accept [[Integer]] argument.

```ruby
[0, 1, 2].minmax # => [0, 2]
['0', '00', '000'].minmax {|a, b| a.size <=> b.size } # => ["0", "000"]
```
## References
1. [ Ruby Docs 3.2: Array / minmax ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-minmax)