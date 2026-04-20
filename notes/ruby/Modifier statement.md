Created: 2023-09-30 10:13

In Ruby, a statement and an [[Expression]] are not the same thing. [[Expression]] is a type of statement. When not used as a modifier, `if`, `else`, `while`, `until`, and `begin` are expressions (and also statements). However, when used as a modifier, `if`, `else`, `while`, `until` and `rescue` are statements but not expressions.

Statements that are not expressions cannot be used in contexts where an expression is expected, such as method arguments:
```ruby
puts( if true; 1 end ) #=> 1
puts( 1 if true )      #=> SyntaxError
```

-------------------------------------------------------------------

"In Ruby there is no clear distinction between statements and expressions" 

"Pretty much everything you write in Ruby is an expression."
## References
1. [Ruby Docs 3.2: syntax/control expressions/Modifier Statements](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-Modifier+Statements)
2. [The Ruby Programming Language: 4. Expressions and Operators](https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/)
3. [Intro to Programming with Ruby: The Basics/Expressions and Return](https://launchschool.com/books/ruby/read/basics#expressionsandreturn)