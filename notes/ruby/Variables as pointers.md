Created: 2023-10-07 13:18

The consequences of an [[Assignment]] depend upon the creation (or not) of a new [[Object]] by the [[Expression]] on the right-hand-side.  
1) When the result of the [[Expression]] on the right-hand-side is a reference to an **existing** [[Object]], not a new one (e.g. a copy of 'self') [[Object passing]] takes place (2nd row of picture).  
2) When the result of the [[Expression]] on the right-hand-side is a **new** [[Object]], the target variable will point to a new place in memory. In case of [[Re-assignment]], it loses the connection it had with any other [[Object]] (1st and 3rd rows of picture).

[[Local variable]]s act as pointers to a physical space in memory. Below is an illustration of what happens ordinarily, "under the hood":
![[Pasted image 20231005123409.png]]

Different spaces/places in memory can hold the same values (the same form of [[Literal]]), but will have different [[Object ID]]. In [[Object passing]], what is being passed is the reference to that space/place.

The same concept has further implications when dealing with [[Collection]]s such as [[Array]]s:
![[Pasted image 20231120141501.png]]

---
Variable as pointers in [[OOP]]:
```ruby
class Pet
  attr_reader :name

  def initialize(name)
    @name = name.to_s
  end

  def to_s
    @name.upcase!
    "My name is #{@name}."
  end
end

name = 'Fluffy'
fluffy = Pet.new(name)
puts fluffy.name # => Fluffy
puts fluffy # => My name is FLUFFY
puts fluffy.name # => FLUFFY
puts name # => FLUFFY
```
The last line in the code above prints the mutated value of the [[String]] because upon the [[Object]]'s instantiation, the return value of the call to `String#to_s` is itself. Since no new [[Object]] is created the [[Local variable]] `name` in the main scope still points to the same place in memory that the instance variable `@name` points to.
## References
1. [Intro to Programming with Ruby: More Stuff/Variables as Pointers](https://launchschool.com/books/ruby/read/more_stuff#variables_as_pointers)