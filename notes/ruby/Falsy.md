Created: 2023-10-04 10:09

A "falsy" value is any value that when evaluated in [[Conditional expression]] will follow the same path as their corresponding [[Boolean]] value: `false`. 

There are only 2 "falsy" values in Ruby:
* `nil`
* `false`

Note that an expression that Ruby _considers false_ is **not** the same as **the** `false` [[Object]].

Using the [[BasicObject]]'s' method `!` twice returns the [[Boolean]] equivalent for "falsy", i.e. `false`.
## References
1. [Ruby Docs 3.2: syntax/control Expressions](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html)
2. [Intro to Programming with Ruby: Flow Control/True and False](https://launchschool.com/books/ruby/read/flow_control#trueandfalse)