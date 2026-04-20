Created: 2023-12-13 08:28

The freeze [[Method]] is meant to avoid [[Object]]s being mutated. It only makes sense to freeze [[Mutable]] [[Object]]s because otherwise they are already frozen:
```ruby
5.frozen? # => true
```

When applied to [[Collection]]s, freeze will **not** keep the state of the [[Object]]s within the [[Collection]]: 
```ruby
arr = ["a", "b", "c"].freeze
arr[2] << "d"
arr # => ["a", "b", "cd"]
```
## References
1. [ courses > RB110 > lesson 2 > 3. Nested Structures](https://launchschool.com/lessons/fa1f5e7e/assignments/fe48f7b1)