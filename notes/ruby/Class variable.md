Created: 2024-01-08 13:39

[[Class]] [[Variable]]s are denoted by two `@` symbols prefixing it, like so: `@@`. Let's create a *class variable* and a [[Class method]] to view that [[Variable]].
```ruby
class GoodDog
  @@number_of_dogs = 0

  def initialize
    @@number_of_dogs += 1
  end

  def self.total_number_of_dogs
    @@number_of_dogs
  end
end

puts GoodDog.total_number_of_dogs   # => 0

dog1 = GoodDog.new
dog2 = GoodDog.new

puts GoodDog.total_number_of_dogs   # => 2
```
We have a [[Class]] [[Variable]] called `@@number_of_dogs`, which upon [[Initialization]] points to 0. Then in our [[Constructor]] (the [[Initialize method]]), we increment that number by 1. Remember that `initialize` gets called every [[Instantiation]] of a new [[Object]] via the [[New method]]. This also demonstrates that we can access [[Class]] [[Variable]]s from within an [[Instance method]] (`initialize` is an [[Instance method]]). Finally, we just return the value of the [[Class]] [[Variable]] in the [[Class method]] `self.total_number_of_dogs`. This is an example of using a class variable and a [[Class method]] to keep track of a [[Class]] level detail that pertains only to the [[Class]], and not to individual [[Object]]s.

Also, within the [[Class]] definition body, a [[Class]] [[Variable]] does **not** have to undergo [[Initialization]] before/above being called/used.

---
They should be **avoided** when working with [[Inheritance]] due to their unintuitive [[Variable Scope]]. As there is only 1 copy of the **class variable** across all sub-[[Class]]es, if the **class variable** undergoes [[Re-assignment]] in any sub-[[Class]] [[Method definition]], the value referenced by it will have changed. That goes against the idea of [[Inheritance]], that [[Super]][[Class]]es affect sub-[[Class]]es but **not** the other way around. The fact that sub-[[Class]]es can override [[Super]][[Class]] **class variables** and the change will affect all other sub-[[Class]]es of the [[Super]][[Class]] is extremely unintuitive behavior.
## References
1. [ LS books / Ruby OOP / classes and objects II ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ courses > RB120 > lesson 3 > 4. Inheritance and Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b8928e96)