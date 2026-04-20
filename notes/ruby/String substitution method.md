Created: 2023-10-25 10:08

These methods perform substitutions:

- [`String#sub`](https://docs.ruby-lang.org/en/3.2/String.html#method-i-sub): One substitution (or none); returns a new [[String]].
- [`String#sub!`](https://docs.ruby-lang.org/en/3.2/String.html#method-i-sub-21): One substitution (or none); returns `self`.
- [`String#gsub`](https://docs.ruby-lang.org/en/3.2/String.html#method-i-gsub): Zero or more substitutions; returns a new [[String]].
- [`String#gsub!`](https://docs.ruby-lang.org/en/3.2/String.html#method-i-gsub-21): Zero or more substitutions; returns `self`.

The first 2 are the best option if you want to **delete** only 1 instance of a pattern (could be 1 character/letter). You can do it by substituting it for an empty [[String]]. [[String.delete]] [[Method]] removes all instances of it.

Each of these methods takes:
- A first argument, `pattern` ([[String]] or regexp), that specifies the substring(s) to be replaced.
- Either of these:
    - A second argument, `replacement` ([[String]] or [[Hash]]), that determines the replacing [[String]].
    - A block that will determine the replacing [[String]].
## References
1. [Ruby Docs 3.2: string/Substitution Methods](https://docs.ruby-lang.org/en/3.2/String.html#class-String-label-Substitution+Methods)
2. [ courses > RB119 > Study Guide for RB119 interview > video 1 ](https://launchschool.com/lessons/a999a6a0/assignments/4d3af2d8)