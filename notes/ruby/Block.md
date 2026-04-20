Created: 2023-09-28 12:24

A block is a piece of code that is delimited by either curly braces `{}` or `do/end` **when** these follow a [[Method invocation]]. Any/all [[Method invocation]] can take a [[Block]]. They are actually *part of* that [[Method invocation]], essentially acting as an **argument** to it, in the same way [[Local variable]]s do. If the [[Block]] is not used then nothing happens (even if it is an **explicit** [[Block]] parameter, unless the [[Local variable]] variable referencing it does `Proc#call`).  They may have [[Block parameter]]s. They create a new pseudo-[[Variable Scope]] rule, the [[Layered Scope]]. It's worth noting that code enclosed in this way does **not always** constitute a block, such as it is the case with [[Control Expression]]s.  The [[Return value]] of a block is the value which its last [[Expression]] evaluates to.

---
Technically any [[Method]] can be called with a block, but the block is only executed if the [[Method definition]] contains the keyword [[Yield]]:
```ruby
def greetings
  puts "Goodbye"
end
word = "Hello"
greetings do
  puts word
end # => 'Goodbye'
```

A [[Block]] can be **passed** and called without [[Yield]] by using an **explicit** [[Block]] parameter:
```ruby
def test2(block)
  puts "hello"
  block.call          # calls the block that was originally passed to test()
  puts "good-bye"
end

def test(&block)
  puts "1"
  test2(block)
  puts "2"
end

test { |prefix| puts "xyz" }
#  1
# hello
# xyz
# good-bye
#  2
```
The `block` [[Local variable]] prepended  with `&`, defined as parameter of `#test`, points to a [[Proc]] [[Object]]. 

`Proc#call` can take arguments that are, themselves, assigned to [[Block parameter]]s just like [[Yield]] does. As a matter of fact, [[Yield]] is pretty much equivalent to [[Proc]].call. Unlike with [[Yield]] though, if an **explicit** [[Block]] gets called within the [[Method definition]] when no [[Block]] was passed in the [[Method call]], the [[Exception]] raised is different. The [[Local variable]] that would be assigned to the [[Proc]] [[Object]] gets assigned to `nil` and it generates the [[Exception]].

---
```ruby
def greetings
  yield
  puts "Goodbye"
end
word = "Hello"
greetings do
  puts word
end # => 'Hello'; 'Goodbye'
```

When designing a [[Method]], at the [[Method definition]] level, writing it with a block, i.e. adding the keyword [[Yield]], will add flexibility in terms of [[Variable Scope]] because when called the method won't be limited to a [[Self-contained Scope]].

---
By convention, `{}` are preferred for single-line blocks whereas `do/end` should be used for multiple line blocks.

Both forms of block have lower [[Precedence]] overall, but `{}` still binds tighter than `do/end`:
```ruby
array = [1, 2, 3]
p array.map { |num| num + 1 }     # => [2, 3, 4]

p array.map do |num|
  num + 1                   #  outputs #<Enumerator: [1, 2, 3]:map>
end                           #  => #<Enumerator: [1, 2, 3]:map>
```
## References
1. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods#whataremethodsandwhydoweneedthem)
2. [Ruby Style Guide: Single-Line Blocks](https://rubystyle.guide/#single-line-blocks)
3. [courses > RB100 > Ruby Style](https://launchschool.com/lessons/7284d88d/assignments/de2630cb)
4. [courses > RB101 > lesson 2 > 19. More Variable Scope](https://launchschool.com/lessons/8a39abff/assignments/1be6d04d)
5. [RB101: Lesson 2 Quiz > Question 12](https://launchschool.com/quizzes/60cdca5b)
6. [ courses > RB110 > lesson 1 > Practice Problems: Methods and More Methods](https://launchschool.com/lessons/6a5eccc0/assignments/f4481ce5)