Created: 2023-09-29 10:54

There's a feature in most programming languages called a procedure, which allows you to extract the common code to one place. In Ruby, we call it a **method**. 

* They are defined in a [[Method definition]].
* They are executed in a [[Method invocation]].
* When capable of altering permanently their caller, they are [[Destructive method]].
* They **do not** obey [[Variable Scope]] rules, i.e. once 'read' by the compiler they are available throughout the program for [[Method call]]. 
* In [[Assignment]], when their [[Return value]] is an existing [[Object]], e.g. self, [[Object passing]] takes place. If their [[Return value]] is a new [[Object]], e.g. a copy of self, then **not**.
## References
1. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods)
2. [Ruby Docs 3.2: syntax/Methods](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html)