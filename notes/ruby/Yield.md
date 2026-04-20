Created: 2024-03-22 14:20

It's a **keyword** used within [[Method definition]]s to call the **implicit** [[Block]] argument (every [[Method call]] has an optional [[Block]] argument).

It allows for a more flexible design by deferring implementation code to [[Method invocation]] decision, i.e. more code can be added *on-the-go*. `Kernel#block_given?` helps in creating this flexibility by enabling a [[Conditional expression]] that keeps the code from breaking. A `LocalJumpError` [[Exception]] is raised if `yield` keyword is used without a [[Block]] in the [[Method call]] (not exactly what happens for **explicit** [[Block]] parameters).

It can have arguments. These will be assigned to the [[Block parameter]]s:
```ruby
def my_method
  yield("baz")
end

my_method { |param| puts param } # => baz
```
[[Block]]s and **yield** parameters have lenient [[Arity]].

---
Sandwich code is a good use-case for [[Block]]s. It is when [[Method]]s perform some "before" and "after" actions. For example:
```ruby
def time_it
  time_before = Time.now
  yield                       # execute the implicit block
  time_after= Time.now

  puts "It took #{time_after - time_before} seconds."
end

time_it { sleep(3) }              # It took 3.003767 seconds.
time_it { "hello world" }         # It took 3.0e-06 seconds.
```
---
A [[Method definition]] can yield to a [[Proc]]:
```ruby
def my_method
  yield
end

proc = Proc.new { puts "I'm executed" }
my_method(&proc) #=> I'm executed
```
## References
1. [ courses > RB130 > lesson 1: blocks > writing methods that take blocks ](https://launchschool.com/lessons/c0400a9c/assignments/5a060a20)