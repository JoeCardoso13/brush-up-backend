Created: 2023-12-08 11:26

Its [[Return value]] is an [[Array]] of [[Integer]]s representing the base-radix digits of the caller. It defaults to base 10 and thence it simply splits up the digits from right to left:
```ruby
12345.digits      # => [5, 4, 3, 2, 1]
```
## References
1. [ Ruby Docs 3.2: Integer / digits ](https://docs.ruby-lang.org/en/3.2/Integer.html#method-i-digits)