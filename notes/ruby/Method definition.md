Created: 2023-09-28 12:05

Have the following syntax: 
```ruby
def my_method(parameter)
  puts "My parameter is #{parameter}"
end
```
The parentheses are also optional, as much as in the [[Method call]], as per [[Ruby's syntactical sugar]]. The body of the code defines a [[Self-contained Scope]]. 

When running, will exit whenever a `return` is reached. If no `return` is reached, the [[Method Invocation]] will evaluate the [[Expression]] of the last line reached and return the result as the method's [[Return value]]. This behavior is similar to [[Control Expression]].

It may have more than one [[Return value]] , as [[Array]], through the following syntax:
```ruby
def my_method()
  num1 = 13
  num2 = 26
  return num1, num2
end
```
## References
1. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods)
2. [Intro to Programming with Ruby: syntax/methods/Scope](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Scope)
3. [Ruby Docs 3.2: syntax/Methods](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html)