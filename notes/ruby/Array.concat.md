Created: 2023-10-24 13:12

Adds to [[Array]] all elements from each argument [[Array]] and [[Return value]] is 'self':
```ruby
a = [0, 1]
a.concat([2, 3], [4, 5]) # => [0, 1, 2, 3, 4, 5]
```
Like using [[Array.push]] and then [[Array.flatten!]] right afterwards.
## References
1. [Ruby Docs 3.2: array/concat](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-concat)
2. [ RB101-119 Small Problems > Easy_8 > all substrings ](https://launchschool.com/exercises/70718e76)