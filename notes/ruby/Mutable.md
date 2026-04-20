Created: 2023-10-06 10:54

**Defined** by having access to [[Destructive method]].

Examples of [[Class]]es that provide [[Instantiation]] of such [[Object]]s:
* [[String]]
* [[Array]]
* [[Hash]]

Essentially, mutable [[Class]]es have [[Setter method]]s that provide access to [[Instance variable]]s, allowing for their [[Re-assignment]]:
```ruby
class Person
  attr_accessor :name

  def initialize(name)
    @name = name
  end
end

sara = Person.new("Sara")
saritcha = sara
saritcha.name = "Saritcha"
p sara.name # => "Saritcha"
```
## References
1. [Variable References and Mutability of Ruby Objects (articles Part 1)](https://launchschool.medium.com/variable-references-and-mutability-of-ruby-objects-4046bd5b6717)
2. [ RB120 / lesson 2 / Quiz / Question 8 ](https://launchschool.com/quizzes/2c1234b5)