Created: 2024-01-10 10:12

If *"everything is an object"* in Ruby, then every [[Method]] is an [[Instance method]]. When making a [[Method call]], Ruby will resolve it by looking into the [[Method lookup path]]. 

Given the following code:
```ruby
class Oracle
  def predict_the_future
    "You will " + choices.sample
  end

  def choices
    ["eat a nice lunch", "take a nap soon", "stay at work late"]
  end
end

class RoadTrip < Oracle
  def choices
    ["visit Vegas", "fly to Fiji", "romp in Rome"]
  end
end

trip = RoadTrip.new
p trip.predict_the_future # => ["visit Vegas", "fly to Fiji", "romp in Rome"].sample
```
The [[Instance method]] `Oracle#choices` was **overridden** by `RoadTrip#choices`.

When a [[Module]] is included in a [[Class]], the [[Class]] is searched before the [[Module]]. But the [[Module]] is searched before the [[Super]][[Class]]. This order of precedence applies to all [[Module]]s and [[Class]]es in the [[Inheritance]] hierarchy.

When including more than 1 [[Module]], Ruby will looks in the reverse order in which they were included. To sum up, using [[Ancestors]]:
```ruby
class GoodDog < Animal
  include Swimmable
  include Climbable
end

puts "---GoodDog method lookup---"
puts GoodDog.ancestors
```
Outputs:
```
---GoodDog method lookup---
GoodDog
Climbable
Swimmable
Animal
Walkable
Object
Kernel
BasicObject
```
Furthermore, if the [[Super]][[Class]] already includes a [[Module]], as is the case in the example above, the **method lookup path** includes it as well, as shown:
```ruby
class Animal
  include Walkable

  def speak
    "I'm an animal, and I speak!"
  end
end
```
## References
1. [ LS books / Ruby OOP / the object model ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#classinheritance)