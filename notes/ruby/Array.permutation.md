Created: 2024-01-04 10:05

When invoked with a [[Block]], yield all permutations of elements from the caller. If given an integer `n` argument, yields the n-tuple permutations to the [[Block]] (`n` defaults to the size of the caller when not given).

```
> arr = 1, 2, 3
 => [1, 2, 3]
> arr.permutation { |x| p x }
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
 => [1, 2, 3]
> arr.permutation(2) { |x| p x }
[1, 2]
[1, 3]
[2, 1]
[2, 3]
[3, 1]
[3, 2]
 => [1, 2, 3]
```

[[Return value]] is the calling [[Object]] itself.
## References
1. [ Ruby Docs 3.2: Array / permutation ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-permutation)