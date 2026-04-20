Created: 2023-10-05 12:15

```
target_variable = expression_return_value_or_reference
```

Defined by the use of a single `=` character. Ruby evaluates the [[Expression]] on the right-hand-side of the `=` character and binds its [[Return value]] to the target variable (usually [[Local variable]]) on the left-hand-side. It can occur in 2 forms: [[Initialization]], when the variable is being created, and [[Re-assignment]], when the variable already exists. 

They are the means through which Ruby exhibits the [[Variables as pointers]] behavior. 

While `=` is not an actual method in Ruby, it acts like one of the non-[[Destructive method]], and should be treated as such. The [[Object]] originally referenced by the left-hand-side variable is **never** mutated by the assignment itself. This is the reason why Ruby is **not** 100% pass by reference language but a [[Pass by copy of reference]].

As a **side effect**, they *always* return the assigned value, i.e. the right-hand-side of `=` [[Expression]], as the [[Return value]] of the assignment [[Expression]]. 
## References
1. [Ruby Docs 3.2: syntax/Assignment](https://docs.ruby-lang.org/en/3.2/syntax/assignment_rdoc.html)
2. [Mutating and Non-mutating Methos in Ruby (articles Part 2)](https://launchschool.medium.com/ruby-objects-mutating-and-non-mutating-methods-78023d849a5f)
3. [ LS books / Ruby OOP / the object model ](https://launchschool.com/books/oo_ruby/read/the_object_model)