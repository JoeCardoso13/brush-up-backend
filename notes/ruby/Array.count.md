Created: 2023-12-08 10:40

**Not** to confuse with [[String.count]]!

Its [[Return value]] is a count of specified elements from [[Array]] caller.

With no argument and no [[Block]], returns the count of all elements:
```ruby
[0, 1, 2].count # => 3
[].count # => 0
```
With [[Object]] argument, counts how many elements of [[Array]] caller are equal to it:
```ruby
[0, 1, 2, 0.0].count(0) # => 2
[0, 1, 2].count(3) # => 0
```
With a [[Block]] **and** no argument, counts how many iterations were evaluated as [[Truthy]]:
```ruby
[0, 1, 2, 3].count {|element| element > 1} # => 2
```
## References
1. [ Ruby Docs 3.2 : Array / count ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-count)
2. [ RB109-RB119 Small Problems > Debugging > TF-IDF ](https://launchschool.com/exercises/4044b772)