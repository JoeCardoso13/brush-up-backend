Created: 2023-10-16 12:18

[`BasicObject`](https://docs.ruby-lang.org/en/3.2/BasicObject.html) is the parent class of all classes in Ruby. It’s an explicit blank class. 

It has 2 noteworthy methods:
* `!` returns the [[Boolean]] negation of [[Object]] caller according to its [[Truthy]] or [[Falsy]] evaluation. Syntax is: `!(Obj_caller) -> true or false`.
* `__id__` (Kernel implements `object_id` for same effect) returns the [[Integer]] that are unique identifiers of the [[Object]]. 
## References
1. [Ruby Docs 3.2: BasicObject](https://docs.ruby-lang.org/en/3.2/BasicObject.html)
2. [RB101-RB109 - Small Problems > Easy 3 > Exclusive Or](https://launchschool.com/exercises/b02d7e27)