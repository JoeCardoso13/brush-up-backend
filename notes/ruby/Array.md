Created: 2023-09-28 10:14

*Arrays are lists of **elements** that are ordered by index, where each element can be any object. Arrays use an integer-based index to maintain the order of its elements.*

* Ordered list of indexed elements. Illustration:
![[Pasted image 20231019122642.png]]
* As per illustration, [[Collection getter (Array)]] (when called with single [[Integer]] argument) returns an existing [[Object]], although different from the Array caller itself.
* It may list [[Local variable]]s as an indexed elements, in which case, according to [[Variables as pointers]], the variable will act as pointer/reference to the actual [[Object]].  
* Syntax for quick array of strings creation: `%w( a b c )`
* Can be created from a [[Range]]:
```ruby
('a'..'c').to_a
=> ["a", "b", "c"]
(1..3).to_a
=> [1, 2, 3]
```
* Can be created implicitly:
```ruby
a = 1, 2, 3 # multiple assignment
p a # prints [1, 2, 3]  
```
## References
1. [Ruby Docs 3.2: Array](https://docs.ruby-lang.org/en/3.2/Array.html)
2. [Intro to Programming with Ruby: The Basics/Basic Data Structures](https://launchschool.com/books/ruby/read/basics)
3. [courses > RB110 > Lesson 1 > 2. Collection Basics](https://launchschool.com/lessons/6a5eccc0/assignments/17756d47)