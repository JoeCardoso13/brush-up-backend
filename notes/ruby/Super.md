Created: 2024-01-09 09:48

Super is used when a [[Behavior]] to be shared from [[Class]] [[Inheritance]] or [[Module]] mixin should be **complemented**. It is a way to add flexibility in sharing [[Behavior]], by neither fully inheriting it, nor fully overriding it.

When you use the keyword `super` from within a [[Method]], it searches the [[Method lookup path]] for a [[Method]] with the same *name*, then invokes it:
```ruby
class Animal
  def speak
    "Hello!"
  end
end

class GoodDog < Animal
  def speak
    super + " from GoodDog class"
  end
end

sparky = GoodDog.new
sparky.speak        # => "Hello! from GoodDog class"
```
Super is commonly used inside the [[Initialize method]]. 

If the **arguments allocation** is not specified by the [[Method definition]], Ruby will pass the [[Method]]'s argument to both [[Super]][[Class]] and sub[[Class]], which may or may not be intended. For example:
```ruby
class Animal
  def initialize
  end
end

class Bear < Animal
  def initialize(color)
    super()
    @color = color
  end
end

bear = Bear.new("black")        # => #<Bear:0x007fb40b1e6718 @color="black">
```
If parenthesis were not specified, it would raise an [[Exception]] due to the number of arguments being incorrect (Animal [[Class]] [[Initialize method]] doesn't take arguments). When the parameters of super are specified though, the **argument allocation** loses all ambiguity. 

**Super** and [[Initialize method]] are, both, **not necessary** in the following scenario:
```ruby
class Animal
  def initialize(diet, superpower)
    @diet = diet
    @superpower = superpower
  end
end

class FlightlessBird < Animal
  def initialize(diet, superpower)
    super
  end
end
```
## References
1. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#classinheritance)
2. [ RB120 - Object Oriented Programming > Debugging > Animal Kingdom ](https://launchschool.com/exercises/14619568)
3. [ RB120 - Object Oriented Programming > Medium 1 > Students ](https://launchschool.com/exercises/a04eaf49)