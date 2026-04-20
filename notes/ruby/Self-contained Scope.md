Created: 2023-09-28 12:45

Its interface with other scopes happen through its parameters and [[Return value]]:
* The only way it gets values from outside itself is through parameters.
* The only way it brings values to outside itself is through the [[Return value]].

In other words, [[Method]] (without [[Block]]) can only access [[Local variable]] whose [[Initialization]] happens inside the method or that are defined as parameters. 

In the following example:
```ruby
def name
  "George"
end
name = "Lisa"
def display_name
  puts name
end

display_name # => "George"
```
Ruby does **not** try to access the local variable `name` because it will never try to access any local variable not initialized within the [[Method definition]] nor given as a parameter. 
## References
1. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods)
2. [courses > RB101 > lesson 2 > 18. Variable Scope](https://launchschool.com/lessons/8a39abff/assignments/e3cd8bb9)