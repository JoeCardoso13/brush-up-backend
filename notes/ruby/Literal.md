Created: 2023-09-27 09:48

Conceptually, a literal is a notation convention that lets you represent value in source code. Examples:
```ruby
'Hello, world!'          # string literal
375                      # integer literal
3.141528                 # float literal
true                     # boolean literal
{ 'a' => 1, 'b' => 2 }   # hash literal
[ 1, 2, 3 ]              # array literal
:sym                     # symbol literal
nil                      # nil literal
(1..13)                  # range literal
```

1. [[String]]
2. [[Integer]]
3. [[Float]]
4. [[Boolean]]
5. [[Hash]]
6. [[Array]]
7. [[Symbol]]
8. [[nil]]
9. [[Range]]

Ruby is an Object Oriented language and even if we pass a literal to a method, Ruby will first convert that literal to an object, then, internally, create a reference to the object. You can think of such literal references as anonymous — unnamed — references.
## References
1. [Intro to Programming with Ruby: The Basics/Literals](https://launchschool.com/books/ruby/read/basics#literals)
2. [Ruby Docs 3.2: syntax/literals](https://docs.ruby-lang.org/en/3.2/syntax/literals_rdoc.html)
3. [Object Passing in Ruby - Pass by Reference or Pass by Value (articles Part 3)](https://launchschool.com/lessons/8a39abff/assignments/20041df9)