Created: 2024-01-08 11:51

It is the [[Accessor method]] responsible for providing a writing interface into the [[Object]] [[State]]:
```ruby
class GoodDog
  def initialize(name)
    @name = name
  end

  def set_name=(name)
    @name = name
  end

  def speak
    "#{@name} says arf!"
  end
end

sparky = GoodDog.new("Sparky")
puts sparky.speak # => Sparky says arf!
sparky.set_name = "Spartacus"
puts sparky.speak # => Spartacus says arf!
```

Even though the [[Method definition]] contains a parentheses, the [[Method call]] does not, thanks to [[Ruby's syntactical sugar]].

---
Notes(**!!!**):

* Setter [[Method]]s **always return the value that is passed in as an argument**, regardless of what happens inside the [[Method]]. If the setter tries to return something other than the argument's value, it just ignores that attempt:
```ruby
class Dog
  def name=(n)
    @name = n
    "Laddieboy"              # value will be ignored
  end
end

sparky = Dog.new()
puts(sparky.name = "Sparky")  # returns "Sparky"
```
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ RB120 - Object Oriented Programming > Debugging > Bank Balance ](https://launchschool.com/exercises/05ac9b2b)