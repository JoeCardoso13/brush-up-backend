Created: 2024-03-23 17:04
### `/(alternating|patterns)/`

After [[Concatenation]], the next step in complexity for **pattern** matching is alternating. To do this we use the [[Meta-character]]s: `(`, `)` and `|`. By separating concatenated **patterns** with pipes and closing all with parentheses we can search for any of them. For example `/(cat|dog|rabbit)/` match occurrences of any of the 3 animals.
## References
1. [ Regular Expressions Book / Basic Matching ](https://launchschool.com/books/regex/read/basic_matching)