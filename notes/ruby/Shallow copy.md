Created: 2023-11-23 11:45

Ruby provides two methods that let us copy an [[Object]], including [[Collection]]s: [`dup`](https://docs.ruby-lang.org/en/3.2/Object.html#method-i-dup) and [`clone`](https://docs.ruby-lang.org/en/3.2/Kernel.html#method-i-clone). Both of these methods create a _shallow copy_ of an [[Object]]. This means that only the [[Object]] that the [[Method]] is called upon is copied. If the object contains other objects - like a nested [[Array]] - then those objects will be **shared**, not copied.

So, for instance:
```ruby
arr1 = ["a", "b", "c"]
arr2 = arr1.dup
arr2[1].upcase!

arr2 # => ["a", "B", "c"]
arr1 # => ["a", "B", "c"]
```
And similarly:
```ruby
arr1 = ["abc", "def"]
arr2 = arr1.clone
arr2[0].reverse!

arr2 # => ["cba", "def"]
arr1 # => ["cba", "def"]
```

The main **difference** between [`dup`](https://docs.ruby-lang.org/en/3.2/Object.html#method-i-dup) and [`clone`](https://docs.ruby-lang.org/en/3.2/Kernel.html#method-i-clone) is that the latter preserves the [[Freeze]] state of the [[Object]]:
```ruby
arr1 = ["a", "b", "c"].freeze
arr2 = arr1.clone
arr2 << "d"
# => RuntimeError: can't modify frozen Array

arr1 = ["a", "b", "c"].freeze
arr2 = arr1.dup
arr2 << "d"
arr2 # => ["a", "b", "c", "d"]
arr1 # => ["a", "b", "c"]
```
## References
1. [ courses > RB110 > lesson 2 > 3. Nested Structures](https://launchschool.com/lessons/fa1f5e7e/assignments/fe48f7b1)