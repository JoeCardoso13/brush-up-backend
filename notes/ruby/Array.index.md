Created: 2023-12-08 10:48

==> A.K.A. [[Array.find_index]]

Its [[Return value]] is the index of a specified [[Array]] caller element.

When argument is given, but no [[Block]]:
```ruby
a = [:foo, 'bar', 2, 'bar']
a.index('bar') # => 1
```
Returns `nil` if no element is found.

When [[Block]] is given, returns the index of the first element for which the [[Block]] returns a [[Truthy]] value:
```ruby
a = [:foo, 'bar', 2, 'bar']
a.index {|element| element == 'bar' } # => 1
```
If no [[Block]] or argument is given, returns [[Enumerator]].
## References
1. [ Ruby Docs 3.2 : Array / index ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-index) 