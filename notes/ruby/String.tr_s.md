Created: 2023-11-16 12:03

Accepts [[Character selector]]s.

There is a [[Destructive method]] version of this [[Method]] with `!` appended.

It substitutes the character just as in [[String.tr]], but then it also squeezes it so that it doesn't repeat.

```ruby
'hello'.tr_s('l', 'r')   #=> "hero"
```
## References
1. [Ruby Docs 3.2: strings/tr_s](https://docs.ruby-lang.org/en/3.2/String.html#method-i-tr_s)
2. [Ruby Docs 3.2: strings/tr_s!](https://docs.ruby-lang.org/en/3.2/String.html#method-i-tr_s-21)