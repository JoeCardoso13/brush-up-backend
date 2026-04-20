Created: 2024-03-25 12:11

`\s` matches whitespace characters and `\S` non-whitespace ones. By definition, the whitespace characters are the space (` `), tab (`\t`), vertical tab (`\v`), carriage return (`\r`), line feed (`\n`), and form feed (`\f`).

`\s` is therefore equivalent to:
```
/[ \t\v\r\n\f]/
```
and `/S`:
```
/[^ \t\v\r\n\f]/
```

They work both in and out [[Character-class]] brackets.
## References
1. [ Regular Expressions Book / Class Shortcuts ](https://launchschool.com/books/regex/read/class_shortcuts)