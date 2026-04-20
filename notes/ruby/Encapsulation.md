Created: 2024-01-08 11:41

**Encapsulation** is hiding pieces of functionality and making it unavailable to the rest of the code base. 

Ruby's [[Object]]s are **strictly** **encapsulated**, i.e. their [[State]] can be accessed only through the [[Method]]s they define. The [[Instance variable]]s manipulated by those [[Instance method]]s cannot be directly accessed from outside the [[Object]]. Example:
```ruby
class MyClass
  def initialize
    @instance_variable = 'instance variable value'
  end
  
  def my_instance_method
    @instance_variable
  end
end

instance_object = MyClass.new
p instance_variable # => Undefined local variable or method error
p instance_object.my_instance_method # => outputs instance variable value
```
Therefore, in an [[OOP]] language like Ruby, [[Method]]s are the interface through which [[Object]]s interact with each other. [[Getter method]]s and [[Setter method]]s are designed to simulate accessing those [[Variable]]s directly. Conventionally, in Ruby, these have the same name as the [[Instance variable]]s they provide access to. Under this context, the latter are often called [[Attribute]]s, and the former, [[Accessor method]]s.

Contrasting with the [[Instance variable]] access described above, [[Instance method]]s are actually [[Public]] by default (with the one and only exception of the [[Constructor]] [[Method]]). Ruby provides a way to implement [[Method access control]] though. 

Keep in mind that [[Class]]es should have as **few** [[Public]] [[Method]]s as possible. It makes it simpler using that [[Class]] and protecting data from undesired changes from the outer world.
## References
1. [The Ruby Programming Language: 7. Classes and Modules](https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/)
2. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
3. [ courses > RB120 > lesson 2 > 6. Lecture: Polymorphism and Encapsulation ](https://launchschool.com/lessons/dfff5f6b/assignments/8c6b8604)