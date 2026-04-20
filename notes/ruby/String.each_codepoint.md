Created: 2023-12-08 09:51

Iterates through the [[ASCII table]] equivalent of each [[String]] caller character and returns itself:
```
> 'abcd'.each_codepoint { |c| p c }
97
98
99
100
 => "abcd"
```

Returns [[Enumerator]] when no [[Block]] is given.
## References
1. [ Ruby Docs 3.2: String / each codepoint ](https://docs.ruby-lang.org/en/3.2/String.html#method-i-each_codepoint)