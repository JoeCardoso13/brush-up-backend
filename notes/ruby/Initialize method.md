Created: 2024-01-08 11:20

It is the [[Constructor]] of the Ruby language.

When only using [[Inheritance]] from a [[Super]] [[Class]], for your [[Object]] [[Instantiation]], i.e. if you are not adding anything to the initialize method of the first initialize found in the [[Method lookup path]], you **don't need to be redundant** (neither Motorcycle nor Car [[Class]]es need the initialize [[Method]]):
```ruby
class Vehicle
  attr_reader :make, :model

  def initialize(make, model)
    @make = make
    @model = model
  end

  def to_s
    "#{make} #{model}"
  end
end

class Car < Vehicle
  def wheels
    4
  end
end

class Motorcycle < Vehicle
  def wheels
    2
  end
end

class Truck < Vehicle
  attr_reader :payload

  def initialize(make, model, payload)
    super(make, model)
    @payload = payload
  end

  def wheels
    6
  end
end
```
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ RB120 - Object Oriented Programming > Easy_1 > refactoring vehicles ](https://launchschool.com/exercises/a4ade9b3)