Created: 2024-03-22 14:03

It is a general concept in computer programming, not something exclusive to Ruby. The idea is to anonymously "enclose" a portion of your code along with its artifacts - i.e. names like [[Variable]]s and [[Method]]s - for future use, through [[Binding]]. This portion of code can then be passed around and executed **later**:
```ruby
name = "Robert"
chunk_of_code = Proc.new {puts "hi #{name}"} # => #<Proc:0x000...
```
Note the above code does **not** execute the code that would output the greeting message to the screen.

The code below demonstrates the full power of **closures**:
```ruby
def sequence
  counter = 0
  Proc.new { counter += 1 }
end

s1 = sequence
p s1.call           # 1
p s1.call           # 2
p s1.call           # 3
puts

s2 = sequence
p s2.call           # 1
p s1.call           # 4 (note: this is s1)
p s2.call           # 2
```
Each invocation of `#sequence` creates a new [[Proc]] [[Object]] that encloses its own copy of `counter` (note that the [[Method definition]] itself does **not** create a closure).

In Ruby, closures are implemented through either:
1) [[Proc]] [[Object]]
2) Lambda
3) [[Block]]
## References
1. [ courses > RB130 > lesson 1: blocks > closures ](https://launchschool.com/lessons/c0400a9c/assignments/0a7a9177) 