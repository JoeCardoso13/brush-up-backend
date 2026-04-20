Created: 2024-01-08 09:59

In Ruby, [[Class]]es can inherit only from a single [[Super]][[Class]], therefore, in cases such as the following:
![[Pasted image 20240110181637.png]]
We would need to write [[Instance method]] *swim* **twice**. Modules come to DRY this. To promote shared [[Behavior]] when there is no clear hierarchical relationship between the [[Class]]es, we use interface [[Inheritance]] with modules. There is no limit to how much modules can be **mixed in** a [[Class]]. 

It's as if we copied and pasted the [[Method]]s right in, except that if we got a [[Class method]] within the module, it doesn't work like that:
```ruby
module Drivable
  def self.drive
    puts "activated!"
  end
end

class Car
  include Drivable
end

Car.drive # => Undefined drive method error
```
And if Ruby is resolving a [[Constant]], also doesn't work like that:
```ruby
module Maintenance
  def change_tires
    "Changing #{WHEELS} tires." # => WHEELS need self.class:: to be found
  end
end

class Vehicle
  WHEELS = 4
end

class Car < Vehicle
  include Maintenance
end

a_car = Car.new
puts a_car.change_tires
# Describe the error and provide two different ways to fix it.
```

---
A module is a collection of [[Behavior]]s that is usable in [[Class]]es or other modules via **mixins**/**interface** [[Inheritance]]. A module is "**mixed** **in**" to a [[Class]] by using the `include` [[Method invocation]].

They'll affect the [[Method lookup path]] though. 

Unlike [[Class]]es, modules do not have access to the [[New method]] (therefore can't provide [[Instantiation]] of new [[Object]]s).

A common naming convention in Ruby is to use the "**able**" suffix on the verb describing the [[Behavior]] that the module is modeling, e.g. `Swimmable`, `Walkable` etc.

You can use [[Accessor method]]s within modules if needed:
```ruby
module Moveable
  attr_accessor :speed, :heading
  attr_writer :fuel_capacity, :fuel_efficiency

  def range
    @fuel_capacity * @fuel_efficiency
  end
end

class WheeledVehicle
  include Moveable
  # ...
end

class Catamaran
  include Moveable
  # ...
end
```
---
The use of **built-in modules** along with specific customized [[Instance method]]s can be quite powerful. For instance:
* Define a custom [[Spaceship operator]] [[Instance method]] and include [[Comparable module]] to enable **comparisons** [[Sorting method]]s etc.
* Define a custom [[each Method]] and include [[Enumerable module]] to enable [[Iteration]]s.

---
2  less common use-cases (other than **mixin**/**interface** [[Inheritance]]) for modules are:

1) [[Namespacing]]
2) [[Method]] container:
```ruby
module Mammal
  # ...

  def self.some_out_of_place_method(num)
    num ** 2
  end
end
```
## References
1. [ LS books / Ruby OOP / the object model ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#classinheritance)
3. [ courses > RB120 > lesson 2 > 10. Lecture: Modules ](https://launchschool.com/lessons/dfff5f6b/assignments/2cf31cc8)