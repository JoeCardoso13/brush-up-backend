Created: 2024-03-25 12:52

`\b` matches word boundaries. A word boundary occurs:
- between any pair of characters, one of which is a word character and one which is not.
- at the beginning of a string if the first character is a word character.
- at the end of a string if the last character is a word character.
`\B` matches non-word boundaries. They occur everywhere else. 

They do **not** work within [[Character-class]] brackets.
## References
1. [ Regular Expressions Book / Class Shortcuts ](https://launchschool.com/books/regex/read/class_shortcuts)