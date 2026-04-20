Created: 2024-01-08 11:49

It is the [[Accessor method]] responsible to provide a reading interface into the [[Object]] [[State]]: 
```ruby
class GoodDog
  def initialize(name)
    @name = name
  end

  def get_name
    @name
  end
end

sparky = GoodDog.new("Sparky")
puts sparky.get_name # => Sparky
```

Getter [[Method]]s typically return a reference to the [[Instance variable]]. 
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ RB120 - Object Oriented Programming > OO Basics: Accessor Methods > avoid mutation ](https://launchschool.com/exercises/ae80cee3)