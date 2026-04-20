Created: 2024-03-16 12:09

The most commonly used format for a regular expression is:
### `/patters/flags`

**Patterns** are what we can use to search for information of interest in a set of [[String]]s. They are the building blocks of regex, not characters or [[String]]s. You can construct complex regex by **concatenating** a series of patterns, and you can analyze a complex regex by breaking it down into its component **patterns**.

At their most basic, the **patterns** are just [[String]]s of characters between two `/` characters, e.g., `/cat/`. This regex matches the [[String]] `cat` anywhere it occurs in some text. It matches `cat`, `scat`, `catalog`, and even `scatter`. The **flags** are mostly language specific. It's worth noting the most common one, the `i`, which makes the **pattern** search *case-insensitive*.

Ruby has a `RegExp#match` [[Method]] for matching regular expressions (also has `=~` **pattern** matching operator). `String#scan` may also come in handy.

Outside of the ordinary alpha-numeric characters, some characters have special meaning. They're the [[Meta-character]]s. There are also a few characters formed by prepending specific letters with [[Backslash character]], they're the [[Control character escape]]s.

The regex engines recognize the following structures of **pattern** searching, in increasing order of complexity:
1) [[Concatenation]]
2) [[Alternation]]
3) [[Character-class]]
## References
1. [ Intro to Regular Expressions / Introduction ](https://launchschool.com/books/regex/read/introduction)
2. [ Ruby Docs 3.2: RegExp > match ](https://docs.ruby-lang.org/en/3.2/Regexp.html#method-i-match)