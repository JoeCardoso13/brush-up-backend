Created: 2023-12-08 11:22

Its [[Return value]] is a 3-elements [[Array]] like so: `[head, match, tail]`
Where the `match` is the argument provided in the [[Method call]], and the `head` and `tail` are the portions of the [[Array]] before and after the `match`, respectively, from left to right:
```ruby
'hello'.partition('l')      # => ["he", "l", "lo"]
```
If no match occurs, returns a copy of itself and 2 empty [[String]]s:
```ruby
'hello'.partition('x') # => ["hello", "", ""]
```

Note: there's also an [[Enumerable.partition]] [[Method]] for [[Collection]]s.
## References
1. [ Ruby Docs 3.2: String / partition ](https://docs.ruby-lang.org/en/3.2/String.html#method-i-partition)