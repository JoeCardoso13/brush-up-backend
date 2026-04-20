Created: 2024-03-23 13:08

Is the surrounding environment/context of an enclosed piece of code. It's how a [[Closure]] keeps **track** of all the information it needs to be executed later. This not only includes [[Local variable]]s, but also [[Method]] references, [[Constant]]s and other artifacts in your code -- whatever it needs to execute correctly, it will drag all of it around.

In the simplest case:
```ruby
def call_me(some_code)
  some_code.call    # call will execute the "chunk of code" that gets passed in
end

name = "Robert"
chunk_of_code = Proc.new {puts "hi #{name}"}

call_me(chunk_of_code) # => hi Robert
```
[[Local variable]] `name`, from the main [[Variable Scope]], was accessible within `#call_me`, even though that should be under [[Self-contained Scope]] (note that `line 6` did not execute the `puts "hi #{name}"` code). To make the point clearer:
```ruby
def call_me(some_code)
  some_code.call
end

name = "Robert"
chunk_of_code = Proc.new {puts "hi #{name}"}
name = "Griffin III"        # re-assign name after Proc initialization

call_me(chunk_of_code) # => hi Griffin III
```
There is a limitation though:
```ruby
def call_me(some_code)
  some_code.call    # call will execute the "chunk of code" that gets passed in
end

chunk_of_code = Proc.new {puts "hi #{name}"}
name = "Robert"

call_me(chunk_of_code) # => undefined local variable or method `name' for main:Object (NameError)
```
The [[Local variable]] has to have undergone [[Initialization]] first.

---
To clarify the limits of the reach of binding, take the following example, here the [[Block]] defines a [[Closure]] and therefore its corresponding binding:
```ruby
ARRAY = [1, 2, 3]

def abc
  a = 3
end

def xyz(collection)
  collection.map { |x| yield x }
end

xyz(ARRAY) do
  # block body, I can reach ARRAY, #abc and #xyz
end
```
In the code above, the [[Block]] does **not** bind to [[Local variable]]s `a` and `collection` living in a [[Self-contained Scope]].

---
Below is a demonstration of the concept of [[Binding]] for [[Block]]s:
```ruby
def sequence
  count = 0
  increase_count { count += 1 }
end
def increase_count(&block)
  block
end

> s1 = sequence
 => #<Proc:0x00007f84c1fe9410 (irb):3>
> s1.call
 => 1
> s1.call
 => 2
> s1.call
 => 3

> s2 = sequence
 => #<Proc:0x00007f84c1f5c6c8 (irb):3>
> s2.call
 => 1
> s2.call
 => 2
```
The [[Binding]] attaches to the [[Local variable]] in the [[Self-contained Scope]] where it was created through the [[Block]]. It then keeps it in a [[Closure]].
## References
1. [ courses > RB130 > lesson 1: blocks > blocks and variable scope ](https://launchschool.com/lessons/c0400a9c/assignments/fd86ea2e)