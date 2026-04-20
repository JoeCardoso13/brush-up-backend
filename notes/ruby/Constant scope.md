Created: 2024-02-21 15:17

The [[Constant]] [[Variable Scope]] do **not** obey [[Layered Scope]] rule, nor [[Self-contained Scope]] rule. They do obey [[Lexical scope]]. When resolving a constant Ruby will look for it, in this order:
1) [[Lexical scope]] (up to main scope)
2) [[Inheritance]] hierarchy of the structure that references the [[Constant]], which is not exactly the [[Method lookup path]], as shown below:
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
  include Maintenance # => Ruby won't search up the method lookup path
end

a_car = Car.new
puts a_car.change_tires
```
3) Main scope
## References
1. [ courses > RB120 > lesson 3 > 4. Inheritance and Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b8928e96)