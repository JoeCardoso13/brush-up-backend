Created: 2024-01-08 11:10

In Ruby, instance [[Variable]]s are denoted by the presence of one `@` character prefixing it. It is what we use to track the [[State]] of [[Object]]s.

They are always attached to an instance [[Object]], i.e. the [[Variable]] is a way to tie data to [[Object]]s. They will "exist" in Ruby's memory, as long as its instance [[Object]], to which it is attached, exists. Using `Object#inspect` on any instance [[Object]] will show, after the [[Class]] name and an encoding of its memory address, a list of its instance variables and their values (usually overridden in built-in [[Class]]es). The [[Object.instance_variables]] [[Method]] can be used to find all instance variables from the [[Object]].  

They can only be accessed (or undergo [[Initialization]]) through [[Instance method]]s, due to Ruby's [[Encapsulation]] strategy.

They can reference any value, be it a custom made [[Object]], a [[String]], a [[Collection]] such as [[Array]] or [[Hash]], an [[Integer]] etc. Depending on the strategy behind how it references another [[Object]], it can be said to be a collaborator [[Object]].

---
Unlike [[Local variable]]s, if we use an instance variable before having undergone [[Initialization]], the [[Return value]] is `nil` instead of [[Exception]]:
```ruby
class Person
  def get_name
    @name
  end
end

bob = Person.new
bob.get_name                  # => nil
```

They **should** only have their [[Initialization]] within [[Instance method]]s. Moreover, they aren't going to have [[Initialization]] unless the [[Instance method]] in which they belong has been called:
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
teddy.swim                                  # => nil
teddy.enable_swimming
teddy.swim                                  # => swimming!
```

They don't undergo [[Inheritance]].
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ courses > RB120 > lesson 3 > 3. Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b4f9e5b7)
3. [ courses > RB120 > lesson 4 > Practice Problems Easy 1 > Question 5 ](https://launchschool.com/lessons/f1c58be0/assignments/a5cfd2ae)