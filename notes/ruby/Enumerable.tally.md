Created: 2023-12-08 10:22

Its [[Return value]] is a [[Hash]] containing the counts of equal elements.
* Each key is an element of the [[Collection]] caller.
* Each value is the number of elements equal to that key.

```ruby
%w[a b c b c a c b].tally # => {"a"=>2, "b"=>3, "c"=>3}
```
With a hash argument, that hash is used for the tally (instead of a new hash), and is returned; this may be useful for accumulating tallies across multiple enumerables:
```ruby
hash = {}
hash = %w[a c d b c a].tally(hash)
hash # => {"a"=>2, "c"=>2, "d"=>1, "b"=>1}
hash = %w[b a z].tally(hash)
hash # => {"a"=>3, "c"=>2, "d"=>1, "b"=>2, "z"=>1}
hash = %w[b a m].tally(hash)
hash # => {"a"=>4, "c"=>2, "d"=>1, "b"=>3, "z"=>1, "m"=> 1}
```
## References
1. [ Ruby Docs 3.2 : Enumerable / tally ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-tally`)