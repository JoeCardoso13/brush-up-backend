Created: 2023-12-08 10:34

Its [[Return value]] is the first element of the [[Collection]] caller for which the [[Block]] returns a [[Truthy]] value:
```ruby
(0..9).find {|element| element > 2}                # => 3
```
If no element is found, returns `nil` by default (can be changed).

With no [[Block]] given, returns [[Enumerator]].
## References
1. [ Ruby Docs 3.2 : Enumerable / find ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-find)