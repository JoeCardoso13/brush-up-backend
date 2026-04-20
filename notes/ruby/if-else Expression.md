Created: 2023-09-29 14:46

* Most common form of [[Control Expression]].
* `then` is optional.
* It **stops** executing when the condition is met. Here only "a is one" is printed:
```ruby 
a = 1

if a == 0
  puts "a is zero"
elsif a == 1
  puts "a is one"
elsif a >= 1
  puts "a is greater than or equal to one"
else
  puts "a is some other value"
end	
```
* Every [[Control Expression]] have a [[Return value]]. When an if-else expression doesn't get executed, it returns `nil`:
```
p( if false
  'whatever'
end)
=> nil
```
* [[Initialization]] of [[Local variable]] to `nil` happens even when the branch is **never** executed:
```ruby
if false
  greeting = "hello world"
end

p greeting # => nil
```
* If you leave one of the [[Conditional expression]]s blank, it returns `nil` even though the branch is ran:
```
> x = 13
> if x > 50
>   p 'executed'
> elsif
>   p '?'
> else
>   p 'reached'
> end
"?"
 => nil
```
* Be aware that, when your condition is guaranteed to return a [[Boolean]] (which should always be), it **does not make sense** to return `true` or `false`, like so:
```ruby
def color_valid(color)
  if color == "blue" || color == "green"
    true
  else
    false
  end # => This doesn't make sense
end
```
## References
1. [Ruby Docs 3.2: syntax/control expressions/If expression](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-if+Expression)
2. [Intro to Programming with Ruby: Flow Control/Conditionals](https://launchschool.com/books/ruby/read/flow_control#conditionals)
3. [courses > RB101 > Lesson 3 > Hard 1 > Question 1](https://launchschool.com/lessons/375f14dd/assignments/567a9e72)
4. [ RB101-RB119 Small Problems > Advanced 1 > Fix the Bug ](https://launchschool.com/exercises/143443fd)