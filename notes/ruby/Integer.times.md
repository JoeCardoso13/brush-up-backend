Created: 2023-10-22 09:18

* [[Return value]] is 'self'.
* Calls the given block `self` times with each integer in `(0..self-1)`:
```ruby
a = []
5.times {|i| a.push(i) } # => 5
a                        # => [0, 1, 2, 3, 4]
```
* With no block given, returns an [[Enumerator]].
## References
1. [Ruby Docs 3.2: integer/times](https://docs.ruby-lang.org/en/3.2/Integer.html#method-i-times)