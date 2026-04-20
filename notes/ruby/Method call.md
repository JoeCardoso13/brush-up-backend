Created: 2023-09-29 11:32

=> A.K.A. [[Method invocation]].

Commonly written like `some_method(obj)` but may have an *explicit caller*, as in `a_caller.some_method(obj)`. The number of arguments must be right according to the [[Method definition]] (it may be flexible if there are [[Default parameter]]). Parenthesis are also optional as per [[Ruby's syntactical sugar]]. 

Will **always** generate a [[Return value]]. If the method exists and the parameters were correct, Ruby executes the lines of the [[Method definition]] in a [[Self-contained Scope]] and returns the value of the last [[Expression]] ran. The `return` keyword exits the [[Method invocation]] enforcing the method's [[Return value]] to be the result of the [[Expression]] next to it. 

When invoked with arguments, [[Object passing]] takes place. 
## References
1. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods)
2. [Ruby Docs 3.2: syntax/Methods](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Methods)
3. [Ruby Docs 3.2: syntax/methods/Return Values](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Return+Values)
4. [Ruby Docs 3.2: syntax/Calling Methods](https://docs.ruby-lang.org/en/3.2/syntax/calling_methods_rdoc.html)