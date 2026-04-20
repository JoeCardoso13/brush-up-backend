Created: 2024-03-13 15:51

When defining a [[Class]], you may create alias method by using the `alias_method` as shown in the example below:
```ruby
  def add(todo)
    raise TypeError, "Can only add Todo objects" if todo.class != Todo
    todos << todo
  end
  alias_method :<<, :add
```
Note that 
1) The `alias_method` line has to be **after** the [[Method definition]] that is being aliased.
2) The order is `alias_method :new, :old`.
## References
1. [ courses > RB130 > lesson 1 > Assignment TodoList ](https://launchschool.com/lessons/c0400a9c/assignments/b2926256)