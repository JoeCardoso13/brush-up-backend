Created: 2024-01-08 10:50

In Ruby, the state of [[Object]]s is tracked through [[Instance variable]]s, i.e. the [[Object]]'s state is saved in its [[Instance variable]]s.

[[Object]]s can be chained as the state of other [[Object]]s, in what is called **collaborator objects** (technically, pretty much any [[Instance variable]] is a *collaborator object* because any value, in Ruby, is an [[Object]], such as a [[String]] or an [[Integer]], which are instances of [[Class]]es themselves). **Collaborator objects** are the [[OOP]] perspective over [[Method chain]]ing. 
## References
1. [ LS books / Ruby OOP / classes and objects I ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ courses > RB120 > lesson 2 > 9. lecture: collaborator objects ](https://launchschool.com/lessons/dfff5f6b/assignments/4228f149)