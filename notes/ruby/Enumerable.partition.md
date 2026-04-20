Created: 2023-12-12 09:48

It returns an [[Array]] of 2 sub-arrays (good for [[Parallel assignment]]). The first having those elements for which the [[Block]] returns a [[Truthy]] value. The other having all other elements. Example:
```ruby
p = (1..4).partition {|ele| ele.even? }
p # => [[2, 4], [1, 3]]
```

Be aware: the [[Block parameter]] is **not** and index! 

Note: careful not to confuse with [[String.partition]].
## References
1. [ Ruby Docs 3.2: Enumerable / partition ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-partition)
2. [ RB110 > lesson 1 > Quizz > Question 18 ](https://launchschool.com/quizzes/7dc41e74)
3. [ RB101-RB119 Small Problems > Easy 6 > Halvsies ](https://launchschool.com/exercises/d9b79537)