Created: 2024-01-09 10:56

**Protected** [[Method]]s are similar to [[Private]] [[Method]]s in that they cannot be invoked outside the [[Class]] definition. When a [[Method]] is [[Private]], the [[Method]] can only be invoked on `self`. However, when a [[Method]] is **protected**, instances of the [[Class]] or a sub[[Class]] can also call the [[Method]]. This means we can easily share sensitive data between instances of the same [[Class]] type. The main difference between them is that protected methods allow access between *class* *instances*, while [[Private]] [[Method]]s do not:
```ruby
class Person
  def initialize(age)
    @age = age
  end

  def older?(other_person)
    age > other_person.age
  end

  protected

  attr_reader :age
end

malory = Person.new(64)
sterling = Person.new(42)

malory.older?(sterling)  # => true
sterling.older?(malory)  # => false

malory.age
  # => NoMethodError: protected method `age' called for #<Person: @age=64>
```
If you change, in the code above, the [[Method invocation]] **protected** to [[Private]], it won't work because on line `age > other_person.age` the access will be denied.

## References
1. [ LS books / Ruby OOP / inheritance ](https://launchschool.com/books/oo_ruby/read/inheritance#classinheritance)