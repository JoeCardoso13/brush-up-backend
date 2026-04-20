Created: 2023-11-16 12:14

There is a [[Destructive method]] version of this [[Method]] with `!` appended.

It removes the characters specified by the [[Character selector]]s. 

```ruby
"hello".delete "l","lo"        #=> "heo"
"hello".delete "lo"            #=> "he"
"hello".delete "aeiou", "^e"   #=> "hell"
"hello".delete "ej-m"          #=> "ho"
```

Use a [[String substitution method]], and substitute for an empty [[String]] instead, if needing to **delete** only 1 instance of occurrence.
## References
1. [Ruby Docs 3.2: string/Delete](https://docs.ruby-lang.org/en/3.2/String.html#method-i-delete)
2. [Ruby Docs 3.2: string/Delete!](https://docs.ruby-lang.org/en/3.2/String.html#method-i-delete-21)
3. [ courses > RB119 > Study Guide for RB119 interview > video 1 ](https://launchschool.com/lessons/a999a6a0/assignments/4d3af2d8)