Created: 2024-03-23 16:26

Most modern computing languages use **control** **character** **escapes** in [[String]]s to represent characters that don't have a visual representation. For example, `\n`, `\r`, and `\t` are nearly universal ways to represent line feeds, carriage returns, and tabs, respectively. [[Regex]] engines support these escapes.

To illustrate:
```
> str = "Jump a\nline ;) \n\tNow I'm tabbed =) \rhey!"
> puts str
Jump a
line ;)
hey!    Now I'm tabbed =)
```

Within [[Character-class]] brackets, you don't need to escape them with [[Backslash character]]. For instance, to search for any character that is not a letter, a space, a carriage return (`\n`), or a line feed (`\r`) you would do `/[^a-z \n\r]/i`.
## References
1. [ Regular Expressions Book / Basic Matching ](https://launchschool.com/books/regex/read/basic_matching)