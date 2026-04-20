Created: 2023-12-08 09:45

It Iterates through the [[String]] caller elements and return it.

Almost equivalent (except for its [[Return value]]) of using [[String.split]] with empty [[String]] argument, then [[each Method]]:
```
3.2.2 :024 > 'abcd'.split('').each { |c| p c }
"a"
"b"
"c"
"d"
 => ["a", "b", "c", "d"]
3.2.2 :025 > 'abcd'.each_char { |c| p c }
"a"
"b"
"c"
"d"
 => "abcd"
```

Returns [[Enumerator]] when no [[Block]] is given.
## References
1. [ Ruby Docs 3.2:  String / each char](https://docs.ruby-lang.org/en/3.2/String.html#method-i-each_char)