Created: 2024-01-19 13:01

Its [[Return value]] is the name of the [[Instance variable]]s of the current [[Object]] in [[Array]] format.

```ruby
class Fruit
  def initialize(name)
    name = name # creating a local variable here
  end
end

class Pizza
  def initialize(name)
    @name = name
  end
end

hot_pizza = Pizza.new("cheese")
orange    = Fruit.new("apple")
```
```
>> hot_pizza.instance_variables
=> [:@name]
>> orange.instance_variables
=> []
```
As the above shows, this [[Method]] doesn't even need a [[Getter method]] to work.
## References
1. [ Ruby Docs 3.2: object/instance_variables ](https://docs.ruby-lang.org/en/3.2/Object.html#method-i-instance_variables)