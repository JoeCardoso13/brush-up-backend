Created: 2024-01-18 11:20

**Lexical scope** means that where the [[Variable]] is defined in the source code determines where it is available, that is, Ruby searches the surrounding structure  of the [[Variable]] reference.

```ruby
class Car
  WHEELS = 4

  def wheels
    WHEELS
  end
end

class Motorcycle < Car
  WHEELS = 2
end

civic = Car.new
puts civic.wheels # => 4

bullet = Motorcycle.new
puts bullet.wheels # => 4, when you expect the out to be 2
```
That is because when [[Instance method]] `Car#wheels` is called, [[Constant]] `WHEELS` that is defined as pointing to `4` is closer than the one pointing to `2`. We can fix it by defining, within the `wheels` [[Method definition]], instead of simply `WHEELS`, the following: `self.class::WHEELS`. This uses the instance [[Object]]'s [[Class]] of the caller to disambiguate the value of the [[Constant]].
## References
1. [ courses > RB120 > lesson 3 > 3. Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b4f9e5b7)