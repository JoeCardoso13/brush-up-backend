Created: 2023-10-24 13:40

Checks the [[String]] caller for a pattern given by first argument. [[Return value]] is [[Boolean]]. Can take optional [[Integer]] as second argument as offset to begin search:
```ruby
'foo'.match?('f', 1) # => false
'foo'.match?('o', 1) # => true
```
## References
1. [Ruby Docs 3.2: string/match?](https://docs.ruby-lang.org/en/3.2/String.html#method-i-match-3F)