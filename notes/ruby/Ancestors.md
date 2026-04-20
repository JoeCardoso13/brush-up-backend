Created: 2024-02-21 14:57

We can use the `::ancestors` [[Class]] [[Method]] on any [[Class]] to find out the **method lookup chain**. 
```ruby
module Speak
  def speak(sound)
    puts "#{sound}"
  end
end

class GoodDog
  include Speak
end

class HumanBeing
  include Speak
end

puts "---GoodDog ancestors---"
puts GoodDog.ancestors
puts ''
puts "---HumanBeing ancestors---"
puts HumanBeing.ancestors
```
Outputs:
```
---GoodDog ancestors---
GoodDog
Speak
Object
Kernel
BasicObject

---HumanBeing ancestors---
HumanBeing
Speak
Object
Kernel
BasicObject
```

## References
1. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#classinheritance)