Created: 2023-12-08 10:06

Computes and returns (as its [[Return value]]) or yields (to [[Block]]) all combinations of elements from all the [[Array]]s, including both caller and arguments:

- The number of combinations is the product of the sizes of all the arrays.
- The order of the returned combinations is indeterminate.

When no [[Block]] is given, returns the combinations as an [[Array]] of [[Array]]s:
```ruby
a = [0, 1, 2]
a1 = [3, 4]
a2 = [5, 6]
p = a.product(a1)
p # => [[0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4]]
p = a.product(a1, a2)
p # => [[0, 3, 5], [0, 3, 6], [0, 4, 5], [0, 4, 6], [1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]
```
When a [[Block]] is given, yields each combination as an [[Array]] and returns the caller:
```
a.product(a1) {|combination| p combination }
[0, 3]
[0, 4]
[1, 3]
[1, 4]
[2, 3]
[2, 4]
```
## References
1. [ Ruby Docs 3.2: Array / product ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-product)