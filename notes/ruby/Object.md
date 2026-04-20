Created: 2023-09-29 11:53

Is the central, foundational concept of the [[OOP]] paradigm. Objects are created from [[Class]]es. Think of [[Class]]es as molds and objects as the things you produce out of those molds.

Objects are **instances** of [[Class]]es. New objects are created through object [[Instantiation]].

---
Excerpts from pre-OO age

* Anything that can be said to have a value is an object: that includes numbers, [[String]]s, [[Array]]s, and even [[Class]]es and modules. However, there are a few things that are not objects: [[Method]]s, [[Block]]s, and [[Variable]]s are three that stand out.

* Instance [[Variable]]s keep track of state, and instance [[Method]]s expose behavior for objects.

* Can be [[Mutable]] or [[Immutable]]. 

* "*An object is a bit of data that has some sort of state — sometimes called a value — and associated behavior. It can be simple, like the [[Boolean]] object `true`, or it can be complex, like an object that represents a database connection.*"

* Ruby is an Object Oriented language and even if we pass a [[Literal]] to [[Method]], Ruby will first convert that literal to an object, then, internally, create a reference to the object. You can think of such literal references as anonymous — unnamed — references.
## References
1. [Variable references and mutability of Ruby objects (articles: Part 1)](https://launchschool.medium.com/variable-references-and-mutability-of-ruby-objects-4046bd5b6717)
2. [Object Passing in Ruby - Pass by Reference or Pass by Value (articles Part 3)](https://launchschool.com/lessons/8a39abff/assignments/20041df9)
3.  [ LS books / Ruby OOP / the object model ](https://launchschool.com/books/oo_ruby/read/the_object_model)