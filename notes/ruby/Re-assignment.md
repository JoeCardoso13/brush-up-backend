Created: 2023-10-05 19:42

Happens when the [[Local variable]] target of the [[Assignment]] [[Expression]], on the left-hand-side, already exists.

If the [[Expression]] on the right-hand-side of the [[Assignment]] returns a new [[Object]], e.g. most operations/[[Method]] from [[Immutable]] classes, the target variable lose the connection with its previous [[Object]] (thus, a new [[Object ID]] is associated to the variable, which references the new [[Object]] in memory). This is notably the case for [[Method]] whose [[Return value]] is a copy of 'self', like the [[Collection getter (String)]] method.

On the other hand, if the [[Expression]] on the right-hand-side of the [[Assignment]] returns a reference to an existing [[Object]], like with most of the [[Destructive method]], then this is a case of [[Object passing]].

**Reassignment** may be subtle if using `+=` (or other assignment operators like `*=`, `+=`, and `%=`):
```ruby
i += 1     # i = i + 1
```
Moreover, when an [[Expression]] like the above occurs and the [[Local variable]] don't exist in the current [[Variable Scope]], we get an [[Exception]] of "*undefined method `+` for nil*", instead of the usual "*undefined local variable or method*". That happens because when we [[Initialization]] of [[Local variable]], they take on a temporary value of `nil` until the right hand side of the assignment [[Expression]] gets evaluated. 

## References
1. [Intro to Programming with Ruby: Variables/Assigning Values to Variables](https://launchschool.com/books/ruby/read/variables#assigningvaluetovariables)
2. [Intro to Programming with Ruby: More Stuff/Variables as Pointers](https://launchschool.com/books/ruby/read/more_stuff#variables_as_pointers)
3. [Ruby Docs 3.2: syntax/Assignment](https://docs.ruby-lang.org/en/3.2/syntax/assignment_rdoc.html)
4. [Mutating and Non-mutating Methos in Ruby (articles Part 2)](https://launchschool.medium.com/ruby-objects-mutating-and-non-mutating-methods-78023d849a5f)
5. [ courses > RB109 > Discussions > When are non-initialized variables assigned to nil?](https://launchschool.com/posts/0ef56477)