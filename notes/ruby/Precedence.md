Created: 2023-10-04 11:58

Determines how Ruby evaluates an [[Expression]]. An operator with greater precedence is said to **bind** more tightly to its operands. Parentheses override the precedence order, will *always* have highest possible precedence. 

In practice, when determining order of precedence of operations in a line of code, you inventory all operands and then **bind** each to the nearest, most concise, [[Expression]] following the *order of precedence*. The commonest ambiguity that leads to erroneous interpretation is with `&&` and `||`. The example below illustrates it using parentheses:
```ruby
num = 12
num % 4 == 0 || num < 7 && num < 10 # => ?
(num % 4 == 0 || num < 7) && num < 10 # => false
num % 4 == 0 || (num < 7 && num < 10) # => true
```

The following is the list of precedence in Ruby, from high to low:
```ruby
!, ~, unary +
**
unary -
*, /, %
+, -
<<, >>
&
|, ^
>, >=, <, <=
<=>, ==, ===, !=, =~, !~
&&
||
.., ...
?, :
modifier-rescue
=, +=, -=, etc.
defined?
not
or, and
modifier-if, modifier-unless, modifier-while, modifier-until
{ } blocks
```
## References
1. [Intro to Ruby Programming Language: Flow Control/Conditionals](https://launchschool.com/books/ruby/read/flow_control#conditionals)
2. [Ruby Docs 3.2: Precedence](https://docs.ruby-lang.org/en/3.2/syntax/precedence_rdoc.html)
3. [RB101: Lesson 2 Quiz > Question 7](https://launchschool.com/quizzes/60cdca5b)