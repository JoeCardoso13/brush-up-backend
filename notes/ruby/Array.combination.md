Created: 2024-01-04 10:10

When invoked with a [[Block]], yield all combinations of elements from the caller. **Cannot** be called without an integer `n` argument, yields the n-tuple combinations to the [[Block]].

```
> arr = 1, 2, 3
 => [1, 2, 3]
> arr.combination(3) { |x| p x }
[1, 2, 3]
 => [1, 2, 3]
> arr.combination(2) { |x| p x }
[1, 2]
[1, 3]
[2, 3]
 => [1, 2, 3]
```

[[Return value]] is the calling [[Object]] itself.

## References
1. [ Ruby Docs 3.2: Array / combination ](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-combination)