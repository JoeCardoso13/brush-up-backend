Created: 2023-10-02 11:06

A range literal is `('a'..'z')` - parenthesis must be included. Although they are mostly used for creating [[Array]], they're a type in an of itself. The example illustrates it:
```ruby
(1..3) == (1...4)
=> false
(1..3).to_a == (1...4).to_a
=> true
```
## References
1. [Ruby Docs 3.2: Range](https://docs.ruby-lang.org/en/3.2/Range.html)
2. [RB101-RB109 - Small Problems > Easy 2 > Odd Numbers](https://launchschool.com/exercises/e7a26cab)