Created: 2024-03-23 15:57

These characters are **not** simply going to match themselves if used bluntly within a regular expression. The regexp engine has a special interpretation for each of them:
`$ ^ * + ? . ( ) [ ] { } | \ /`

If needing to match one of these meta-characters literally, you must escape (prepend) it with a leading [[Backslash character]]: `\`.

Notably:
1) [[Range-of-characters]]
2) [[Negated-classes]]
3) [[Any-character]]
4) [[Whitespace]]
5) [[Word-characters]]
6) [[Word-boundaries]]
## References
1. [ Regular Expressions Book / Basic Matching ](https://launchschool.com/books/regex/read/basic_matching)