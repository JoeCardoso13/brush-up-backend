Created: 2024-01-08 12:43

It is required when using [[Setter method]] to change [[Attribute]], otherwise Ruby creates a [[Local variable]]. 

Ruby convention is to use it only when required.

---

Within the body of a [[Class]], but outside any [[Instance method]]s defined by the [[Class]], the `self` keyword refers to the [[Class]] being defined:
```
> class DearJoe
>   puts self
> end
# Upon class definition:
DearJoe # => printed
=> nil  # => returned
```
---

Within the body of an [[Instance method]] definition it refers to the [[Object]] instance responsible for the [[Method call]].
```
> class MyJoe
>   def my_method
>     puts self
>   end
> end

> Joe = MyJoe.new
=> #<MyJoe:0x00007ffba3a1b5c0>
> Joe.my_method
#<MyJoe:0x00007ffba3a1b5c0>
```
---

Apparently, within the parameters of an [[Instance method]], i.e. as a [[Default parameter]], it refers to the **instance** [[Object]], not [[Class]]:
```ruby
class Shelter
  # ...
  def adopt(owner = self, pet)
    owner.pets << pet
  end
  # ...
end
```
---

When prepending a [[Method]]'s name upon its [[Method definition]] within a [[Class]], it refers to the [[Class]] itself, therefore the [[Method]] becomes a [[Class method]]. Moreover, when within a [[Class method]], unlike when it's within the body of an [[Instance method]] definition, it **also** refers to the [[Class]]. 

Take this code, for instance:
```ruby
class MeMyselfAndI
  self

  def self.me
    self
  end

  def myself
    self
  end
end

i = MeMyselfAndI.new
```
Out of the 4 times it shows up, `self` refers to an instance [[Object]] only in its last appearance (line 9).
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ Ruby Style Guide / explicit self ](https://rubystyle.guide/#no-self-unless-required)
3. [The Ruby Programming Language: 7. Classes and Modules](https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/)