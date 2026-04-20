Created: 2023-12-08 11:19

Its [[Return value]] is an [[Array]] where the elements are [[Integer]]s corresponding to the [[ASCII table]] conversion of each character of the [[String]] caller:
```ruby
'hello'.codepoints     # => [104, 101, 108, 108, 111]
```

Equivalent to using [[String.chars]], [[map Method]] and [[String.ord]] in each [[Block]]'s [[Iteration]] (possibly shortened by [[Ruby's syntactical sugar]]) in a [[Method chain]]:
```ruby
'hello'.chars.map(&:ord) # => [104, 101, 108, 108, 111] 
```
## References
1. [ Ruby Docs 3.2: String / codepoints ](https://docs.ruby-lang.org/en/3.2/String.html#method-i-codepoints)
2. [ RB101-RB119 - Small Problems > Easy 5 > ASCII value ](https://launchschool.com/exercises/ae82edb6)