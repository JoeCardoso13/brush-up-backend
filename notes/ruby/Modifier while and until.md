Created: 2023-09-30 09:43

* [[while Loop]]s and [[until Loop]]s can be used as one-liners like [[Modifier if and unless]]: 
```ruby
a += 1 while a < 10
a += 1 until a > 10
```
* You can use `begin` and `end` to create to create a **loop** that runs at least once (against Ruby Style Guide):
```ruby
a = 0
begin
  a += 1
end while a < 10
p a # prints 10
```
## References
1. [Ruby Docs 3.2: syntax/control expressions/Modifier while and until](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-Modifier+while+and+until)
2. [Ruby Style Guide: loop-with-break](https://rubystyle.guide/#loop-with-break)