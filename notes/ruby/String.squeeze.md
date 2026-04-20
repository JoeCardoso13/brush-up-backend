Created: 2023-11-16 12:17

There is a [[Destructive method]] version of this [[Method]] with `!` appended.

Each of the duplicate, subsequent, occurrence of [[Character selector]] is eliminated.

```ruby
"yellow moon".squeeze                  #=> "yelow mon"
"  now   is  the".squeeze(" ")         #=> " now is the"
"putters shoot balls".squeeze("m-z")   #=> "puters shot balls"
```
## References
1. [Ruby Docs 3.2: string/Squeeze](https://docs.ruby-lang.org/en/3.2/String.html#method-i-squeeze)
2. [Ruby Docs 3.2: string/Squeeze!](https://docs.ruby-lang.org/en/3.2/String.html#method-i-squeeze-21)