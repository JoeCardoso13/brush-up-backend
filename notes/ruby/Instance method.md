Created: 2024-01-08 11:27

Instance methods are custom [[Method definition]]s within a [[Class]] definition. They are are [[Public]] by default as per Ruby's [[Encapsulation]] strategy.

---
When calling these [[Method]]s Ruby will resolve it with the [[Method lookup path]]. The [[Lexical scope]] is ignored, as the following illustrates:
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
trip.predict_the_future # => :choices resolves from RoadTrip
```

They need an instance [[Object]] of the same [[Class]] to effectuate the [[Method call]], otherwise they don't work:
```ruby
class Greeting
  def greet(message)
    puts message
  end
end

class Hello < Greeting
  def self.hi
    greet("Hello")
  end
end

Hello.hi # => Error!
```
---
Be careful not to violate the DRY principle when defining your instance method. The example below illustrates a violation:
```ruby
class Light
  attr_accessor :brightness, :color

  def initialize(brightness, color)
    @brightness = brightness
    @color = color
  end

  def light_status
    "I have a brightness level of #{brightness} and a color of #{color}"
  end
end
```
`light_status` should be changed to `status` to keep it DRY.
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#methodlookup)
3. [ courses > RB120 > lesson 4 > PP: Easy 1 > Question 7 ](https://launchschool.com/lessons/f1c58be0/assignments/a5cfd2ae)