Created: 2024-01-08 09:43

**Polymorphism** is the ability for different types of data to respond to a common interface. For instance, if we have a [[Method]] that invokes the `#move` [[Method]] from its argument, we can pass the [[Method]] any type of argument as long as the argument has a compatible `#move` [[Method]]. The [[Object]] might represent a human, a cat, a jellyfish, or, conceivably, even a car or train. That is, it lets [[Object]]s of different types respond to the same [[Method]] invocation. When we don't care what type of [[Object]] is calling the [[Method]], we're using **polymorphism** (here with [[Duck typing]]):
```ruby
class MyClass1
  def a_method
    puts "does something"
  end
end

class MyClass2
  def a_method
    puts "does something else"
  end
end

obj1, obj2 = MyClass1.new, MyClass2.new
[obj1, obj2].each { |obj| obj.a_method }
```

In practice, **Polymorphism** happens in 2 ways:

* Through [[Inheritance]]:
When **overriding** [[Instance method]]s in sub[[Class]]es to add specificity, we also enable them to be polymorphically called:
```ruby
class Animal
  def move
  end
end

class Fish < Animal
  def move
    puts "swim"
  end
end

class Cat < Animal
  def move
    puts "walk"
  end
end

# Sponges and Corals don't have a separate move method - they don't move
class Sponge < Animal; end
class Coral < Animal; end

animals = [Fish.new, Cat.new, Sponge.new, Coral.new]
animals.each { |animal| animal.move }
```
**Interface inheritance** is another way of using [[Inheritance]] to apply **polymorphism**. In addition to using class inheritance to implement polymorphism, we can also use mixin modules to implement polymorphism through inheritance via classes that are not related:
```ruby
module Coatable
  def coating
    "I'm covered in chocolate"
  end
end

class JaffaCake
  include Coatable         # mixing in Coatable module
end

class Raisin
  include Coatable         # mixing in Coatable module
end

snacks = [JaffaCake.new, Raisin.new]
snacks.each { |snack| puts snack.coating }
```

* Through [[Duck typing]]

In practice, **polymorphic** [[Method]]s are intentionally designed to be **polymorphic**; if there's no intention, you probably shouldn't use them **polymorphically**.
## References
1. [ LS books / Ruby OOP / the object model ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ courses > RB120 > lesson 2 > 6. Lecture: Polymorphism and Encapsulation ](https://launchschool.com/lessons/dfff5f6b/assignments/8c6b8604)
3. [ RB120 - Object Oriented Programming > Easy 2 > moving ](https://launchschool.com/exercises/aabd5d59)