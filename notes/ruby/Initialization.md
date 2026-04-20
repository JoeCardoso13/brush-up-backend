Created: 2023-10-05 19:37

It's when an [[Assignment]] happens and the left-hand-side target variable (often [[Local variable]]) didn't exist before. It **defines** the [[Variable Scope]] based on the context of its creation. 

The variable will then be assigned an [[Object ID]], which is the **reference** to the value it points to.

---
##### Bug Advice
Might happen to [[Local variable]]s inadvertently. E.g. happens in [[Control Expression]]s even when its code is **not** executed. Here's an example for [[if-else Expression]]:
```ruby
while false do
  a = 13
end
p a # => nil
```
Or if Ruby disambiguates a [[Local variable]] from an [[Accessor method]]:
```ruby
# ...

  def display_high_priority_tasks
    tasks = tasks.select do |task|
      task.priority == :high
    end

    display(tasks)
  end

# ...
```
---
It's worth noting how [[Instance variable]]s **contrast** to [[Class variable]]s in regards to their initialization:
```ruby
class Person
  @name = "bob"              # class level initialization

  def get_name
    @name
  end
end

bob = Person.new
bob.get_name                  # => nil
```
Otherwise [[Instance variable]]s behave (somewhat) similar to [[Local variable]]s in regards to initialization:
```ruby
module Swim
  def enable_swimming
    @can_swim = true
  end
end

class Dog
  include Swim

  def swim
    "swimming!" if @can_swim
  end
end

teddy = Dog.new
p teddy.swim # => nil
teddy.enable_swimming
p teddy.swim # => "swimming!"
```
## References
1. [Ruby Docs 3.2: syntax/Assignment](https://docs.ruby-lang.org/en/3.2/syntax/assignment_rdoc.html)
2. [courses > RB101 > lesson 2 > 18. Variable Scope](https://launchschool.com/lessons/8a39abff/assignments/e3cd8bb9)
3. [RB101 > Lesson 3 > Practice Problems Hard > Q1](https://launchschool.com/lessons/375f14dd/assignments/567a9e72)
4. [ courses > RB120 > lesson 3 > 4. Inheritance and Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b8928e96)
5. [ RB120 Object Oriented Programming > Debugging > Task Manager ](https://launchschool.com/exercises/c7952581)