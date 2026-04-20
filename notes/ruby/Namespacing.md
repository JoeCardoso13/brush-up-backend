Created: 2024-02-26 15:54

**Namespace** is a way to avoid collision when [[Class]]es have the same names:
```ruby
module Transportation
  class Vehicle
  end

  class Truck < Vehicle
  end

  class Car < Vehicle
  end
end

module Toys
  class Truck
  end

  class Car
  end
end

Transportation::Truck != Toys::Truck # => true
```

We call [[Class]]es in a [[Module]] by appending the [[Class]] name to the [[Module]] name with two colons(`::`).

## References
1. [ RB120 - Object Oriented Programming > OO Basics Inheritance > Transportation ](https://launchschool.com/exercises/507a7449)