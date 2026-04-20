Created: 2024-01-09 10:52

Sometimes you'll have [[Method]]s that are doing work in the [[Class]] but don't need to be available to the rest of the program. These methods can be defined as **private**. How do we define private methods? We use the `Module#private` [[Method call]] in our [[Class]] and anything below it is private (unless another method, like [[Protected]], is called after it to negate it).
## References
1. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#classinheritance)
2. [ RB120 - Object Oriented Programming > Medium 1 > Privacy ](https://launchschool.com/exercises/d0f9783f)