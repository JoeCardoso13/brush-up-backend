Created: 2024-01-08 09:52

**Inheritance** is a way to share [[Behavior]] between [[Class]]es, it is a way to apply the DRY principle.

There are **2** distinct kinds of **inheritance** in Ruby: one is defined with `<` and [[Super]] and the other is with [[Module]] and `include` keyword. They're called [[Class]] **inheritance** and **interface** inheritance, respectively.  Here are a couple of things to consider when choosing:

- You can only sub[[Class]] (class inheritance) from one class. You can mix in as many [[Module]]s (interface inheritance) as you'd like.
- If there's an "is-a" relationship, **class** **inheritance** is usually the correct choice. If there's a "has-a" relationship, **interface** **inheritance** is generally a better choice. For example, a dog "is an" animal and it "has an" ability to swim.
- You cannot instantiate [[Module]]s. In other words, [[Object]]s cannot be created from [[Module]]s.

All custom [[Class]]es will inherit from the [[Object]] [[Class]]. Except for the `Object#to_s`, the [[Instance method]]s of this [[Class]] can bring serious consequences if **overridden** accidentally (say, for instance, `Object#instance_of?` or `Object#send`).

---
#### [[Class]] inheritance

If they have a clearly hierarchical relationship, i.e. the sub-[[Class]] "is-a" layer of specificity on top of the [[Super]][[Class]], they're suited for [[Class]] inheritance:
```ruby
class Theater
  def seats; end
  def screen; end
end

class ThreeDTheater < Theater
  def glasses; end
end

puts ThreeDTheater.instance_methods.include?(:glasses) # => true
puts ThreeDTheater.instance_methods.include?(:screen) # => true
puts ThreeDTheater.instance_methods.include?(:seats) # => true
```
We create inheritance using `<` when defining the [[Class]]:

In this example the `ThreeDTheater` [[Class]] is inheriting all [[Method]]s from its superclass `Theater`. If `ThreeDTheater` happens to have any [[Instance method]] of the same name as a `Theater` one, it will **override** it (see [[Method lookup path]]). If the intention is to only **partly override**, but to complement, as well, the [[Super]][[Class]] [[Method]], Ruby provides the keyword [[Super]].

---
#### Interface inheritance

To share [[Behavior]] more flexibly, we use **interface inheritance**. It allows [[Class]]es to inherit certain [[Behavior]] only when needed, on a case-by-case basis. 

Any time a [[Behavior]] is to be shared among [[Class]]es, however it is **not** to be shared to other [[Class]]es, and these classes already use [[Class]] **inheritance**, it is time to use **interface inheritance**. Example:
```ruby
module Swimmable
  def swim
    "I'm swimming!"
  end
end

class Animal; end

class Fish < Animal
  include Swimmable         # mixing in Swimmable module
end

class Mammal < Animal
end

class Cat < Mammal
end

class Dog < Mammal
  include Swimmable         # mixing in Swimmable module
end
```
Here the method `#swim` is to be included on both Dog and Fish [[Class]]es, but cannot be included in the Cat class, whereas these already have [[Class]] inheritance for others, suitable, [[Behavior]]s.
## References
1. [ LS books / Ruby OOP / the object model ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#classinheritance)