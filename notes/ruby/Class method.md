Created: 2024-01-08 13:22

Class methods are [[Method]]s we can call directly on the [[Class]] itself, without having [[Instantiation]] of any [[Object]]s. It is meant to be used when [[Behavior]] is independent of [[State]]. 

Use [[Self]] keyword when defining the class [[Method]] by prepending it to the [[Method definition]]'s name:
```ruby
# ...
  def self.my_class_method
    # body of method
  end
# ...
```
But remember this is a convention. It would work just as well (although against established practice) to do as follows:
```ruby
class MyClass
  def MyClass.my_class_method # => equivalent to self.my_class_method
    # body of the method
  end
end
```

You can call a [[Class]] [[Method]] with either syntax: `Class::method` or `Class.method`.
## References
1. [ LS books / Ruby OOP / classes and objects II ](https://launchschool.com/books/oo_ruby/read/the_object_model)