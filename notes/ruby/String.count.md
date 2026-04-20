Created: 2023-11-16 12:12

**Not** to confuse with [[Array.count]]!

Returns the total number of characters in `self` that satisfy the [[Character selector]]s criteria.

```ruby
a = "hello world"
a.count "lo"                   #=> 5
a.count "lo", "o"              #=> 2
a.count "hello", "^l"          #=> 4
a.count "ej-m"                 #=> 4
```
## References
1. [Ruby Docs 3.2: string/Count](https://docs.ruby-lang.org/en/3.2/String.html#method-i-count)
2. [ courses > RB119 > Study Guide for Interview > video 4 (2nd) ](https://launchschool.com/lessons/a999a6a0/assignments/4d3af2d8)