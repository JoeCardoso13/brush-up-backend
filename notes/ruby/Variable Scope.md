Created: 2023-09-28 11:59

They determine where variables can be used. They are determined by where the variable [[Initialization]] takes place (and the [[Types of variables]]).

## Local variables
In practice, it is like there are 2 types of [[Local variable]] scope: [[Self-contained Scope]] and [[Layered Scope]]. However, the latter is a characteristic of [[Binding]] and the former is the **scope** itself, properly defined.
## Instance variables
[[Instance variable]]s are scoped at the [[Object]] level. They do not cross over between [[Object]]s. They are 'attached' to a particular instance [[Object]] and will exist as log as the [[Object]] itself exists.

It's worth noting that they do **not** obey either [[Self-contained Scope]] or [[Layered Scope]], as the following code demonstrates:
```ruby
class Person
  def initialize(n)
    @name = n
  end

  def get_name
    @name       # is the @name instance variable accessible here?
  end
end

bob = Person.new('bob')
bob.get_name                  # => "bob"
```

## Class variables
[[Class variable]]s are scoped at the [[Class]] level. They exhibit 2 main behaviors:
- all [[Object]]s share 1 copy of the [[Class]] [[Variable]]. (This also implies [[Object]]s can access [[Class]] [[Variable]]s by way of [[Instance method]]s.)
- [[Class method]]s can access a [[Class]] [[Variable]] provided the [[Class]] [[Variable]] has undergone [[Initialization]] prior to the [[Method call]].
```ruby
class Person
  @@total_people = 0            # initialized at the class level

  def self.total_people
    @@total_people              # accessible from class method
  end

  def initialize
    @@total_people += 1         # reassigned from instance method
  end

  def total_people
    @@total_people              # accessible from instance method
  end
end

Person.total_people             # => 0
Person.new
Person.new
Person.total_people             # => 2

bob = Person.new
bob.total_people                # => 3

joe = Person.new
joe.total_people                # => 4

Person.total_people             # => 4
```

## Constants
[[Constant]]s are first searched in the [[Lexical scope]] up to, **but not including**, the **main scope**, and then in the [[Method lookup path]]:
```ruby
class Vehicle
  WHEELS = 4
end

WHEELS = 6

class Car < Vehicle
  def wheels
    WHEELS
  end
end

car = Car.new
puts car.wheels        # => 4
```
Still, if the [[Constant]] wasn't found, Ruby will look for it in the **main scope**:
```ruby
class Vehicle
end

WHEELS = 6

class Car < Vehicle
  def wheels
    WHEELS
  end
end

car = Car.new
puts car.wheels        # => 6
```

## Methods
[[Method]]s aren't [[Object]]s, they **do not** obey variable scoping rules, i.e. once the [[Method definition]] is 'read' by the compiler, they are available throughout the program for [[Method call]]s. 
## References
1. [Intro to Programming with Ruby: Variables](https://launchschool.com/books/ruby/read/variables#variablescope)
2. [Intro to Programming with Ruby: syntax/methods/Scope](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Scope)
3. [ courses > RB120 > lesson 3 > 3. Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b4f9e5b7)
4. [ courses > RB120 > lesson 3 > 4. Inheritance and Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b8928e96)