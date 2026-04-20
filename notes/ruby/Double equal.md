Created: 2024-03-25 13:52

Usually it is a built-in [[Method]] for standard library [[Class]]es that is meant to check for the equivalence of **values** between 2 [[Object]]s:
```ruby
str1 = "something"
str2 = "something"
str1 == str2            # => true

int1 = 1
int2 = 1
int1 == int2            # => true

sym1 = :something
sym2 = :something
sym1 == sym2            # => true
```
However, when defining a custom [[Class]], if `#==` is not defined its [[Method call]] will follow the [[Method lookup path]] until it reaches the [[BasicObject]], where the definition is based on [[Object ID]]:
```ruby
class Person
  attr_accessor :name
end

bob = Person.new
bob.name = "bob"

bob2 = Person.new
bob2.name = "bob"

bob == bob2                # => false

bob_copy = bob
bob == bob_copy            # => true
```
By the way, when defining a custom `#==` for your [[Class]], Ruby gives, automatically, a `!=`.

It is used for *Minitest*'s `#assert_equal`.
## References
1. [ courses > RB120 > lesson 3 > 2. Equivalence ](https://launchschool.com/lessons/d2f05460/assignments/9cadd494)