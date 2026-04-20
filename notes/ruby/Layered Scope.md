Created: 2023-09-28 12:46

Created/defined by a [[Block]].

Inner scope can access variables initialized in an outer scope, but not vice versa. This can go on through different levels/layers. 

[[Variable shadowing]] may prevent access to outer scope [[Local variable]].

Peer scopes do not conflict, i.e. [[Local variable]] with [[Initialization]] in an inner scope will **not** be accessible on a parallel scope:
```ruby
2.times do
  a = 'hi'
  puts a      # 'hi' <= this will be printed out twice due to the loop
end

loop do
  puts a      # => NameError: undefined local variable or method `a' for main:Object
  break
end
```

[[Method]]s **do not** obey this scoping rule. Example:
```ruby
loop do
  def name
    "George"
  end
  break
end

puts name # => George
```
---
Turns out this scoping rule is useful as a rule of thumb, for practical purposes, but perhaps not 100% correct, strictly speaking. This is more of a characteristic of [[Binding]] than a different kind of scope in and of itself. The code within the [[Block]] defines a [[Closure]] that gets its [[Binding]] from the **outer-layer**.
## References
1. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods#whataremethodsandwhydoweneedthem)
2. [courses > RB101 > lesson 2 > 18. Variable Scope](https://launchschool.com/lessons/8a39abff/assignments/e3cd8bb9)