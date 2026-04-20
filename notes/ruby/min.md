Created: 2023-12-26 10:57

Both [[Array]] class and [[Enumerable module]] contain this [[Method]]. 

This is effectively a shortcut for using [[Array.sort]] (or [[Hash.sort]]) and then picking first place. Analogously, [[min_by]] relates to [[Array.sort_by]] (or [[Hash.sort_by]]). Using an [[Integer]] argument into an [[Array]] of mins.

```
> ['0', '00', '000'].min { |a, b| a.size <=> b.size } # => "0"
=> ["0", "00"]
```
## References
1. [ courses > RB119 > Study Guide for RB119 interview > video 1 ](https://launchschool.com/lessons/a999a6a0/assignments/4d3af2d8)
2. [ Ruby Docs 3.2: Array / min ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-min)