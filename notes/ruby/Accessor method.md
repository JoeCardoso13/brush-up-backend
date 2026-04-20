Created: 2024-01-08 12:21

Are the [[Setter method]]s and [[Getter method]]s used to access [[Instance variable]]s.

The use of [[Getter method]] and [[Setter method]] is so common that Ruby provides shorthand syntax for that. Using [[Method]]s `attr_reader`, `attr_writer` and `attr_accessor` followed by the [[Instance variable]] names in [[Symbol]] type (conventionally preferred over, also possible, [[String]]) we create, automatically, a [[Getter method]], a [[Setter method]] or both, respectively, along with the respective [[Instance variable]], to access the named [[Attribute]]s.
```ruby
attr_accessor :name, :height, :weight
```
This one line of code gives us six getter/setter [[Instance method]]s: `name`, `name=`, `height`, `height=`, `weight`, `weight=`. It also gives us three [[Instance variable]]s: `@name`, `@height`, `@weight` (although these won't incur [[Initialization]] until their code is executed).

In order to access the [[Instance variable]]'s value, it is *standard practice* to use the **accessor method**, instead of the [[Variable]] itself, because it makes maintenance so much easier.

However extra caution must be taken for the [[Setter method]]. They must be called by [[Self]] otherwise Ruby will treat the [[Expression]] as [[Variable]] [[Assignment]]. Example:
```ruby
def change_info(n, h, w)
  self.name = n
  self.height = h
  self.weight = w
end
```
Moreover, do not abuse the use of [[Setter method]]s, [[Getter method]]s and [[Local variable]]s by naming them similarly. A name **can't** mean different things on a single [[Assignment]] [[Expression]] (see [[Initialization]] *bug* *advice*).
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ courses > RB120 > lesson 4 > Practice Problems Easy 2 > Question 4 ](https://launchschool.com/lessons/f1c58be0/assignments/25448951)