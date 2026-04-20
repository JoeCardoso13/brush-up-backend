Created: 2024-03-23 16:53
### `/[alternating_patterns]/`

Using brackets to enclose characters is the equivalent of using [[Alternation]] for each one of them. The [[Regex]] `/[abc][12]/` matches any two characters (word) where the first character is an `a`, `b`, or `c`, and the second is a `1` or a `2`.

Under the context of **character-class**, i.e. inside brackets, the [[Meta-character]]s dwindle to `^` `\` `-` `[` `]`. Still, some of these are only [[Meta-character]]s in certain situations.
## References
1. [ Regular Expressions Book / Character Classes ](https://launchschool.com/books/regex/read/character_classes)