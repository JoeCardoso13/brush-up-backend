Created: 2023-11-20 13:03

# `String#<=>`

When comparing [[String]]s, the comparison is character-by-character. Ruby moves from left-to-right in the strings looking for the first character that is different from its counterpart in the other string. Once it finds a character that differs, it compares that character with its counterpart using the [[Spaceship operator]] which, in this case, uses the [[ASCII table]] to determine the outcome. If both strings are equal up to the length of the shorter string, then the criterion changes to [[String]] length.

```ruby
['arc', 'bat', 'cape', 'ants', 'cap'].sort
# => ["ants", "arc", "bat", "cap", "cape"]
```

It's tricky when dealing with [[String]]s of [[Integer]]s of different lengths:
```
> %w( 9 78 234 6 231 77 ).sort
 => ["231", "234", "6", "77", "78", "9"]
```
## References
1. [Ruby Docs 3.2: string/Comparing](https://docs.ruby-lang.org/en/3.2/String.html#class-String-label-Methods+for+Comparing)
2. [courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)