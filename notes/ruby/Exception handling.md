Created: 2024-01-19 10:10

A `begin/rescue/end` block (**not** a `do/end` [[Block]]) can avoid the code from breaking:
```ruby
begin  
	# put code at risk of failing here  
rescue TypeError  
	# take action  
end
```
If `TypeError` wasn't specified, it would default to `StandardError`. 

You should **never** handle **errors** from the [[Exception]] [[Class]] itself, i.e. (see [[Exception class hierarchy]]) all possible **errors**.

---
There can be multiple `rescue` clauses or [[Exception]] types:
```ruby
begin  
	# some code at risk of failing  
rescue TypeError  
	# take action  
rescue ArgumentError  
	# take a different action  
end

begin  
	# some code at risk of failing  
rescue ZeroDivisionError, TypeError  
	# take action  
end
```
---
To assign the [[Exception]] [[Object]], use the following syntax:
```ruby
rescue TypeError => e
```
Conventionally they're always assigned to `e`. E.g. taking advantage of some of Ruby's built-in [[Exception]] [[Instance method]]s:
```ruby
begin  
	# code at risk of failing here  
rescue StandardError => e # storing the exception object in e  
  puts e.message # output error message  
end
```
We can also use `Object#class`

---
The `ensure` clause will have its branch always executed:
```ruby
file = open(file_name, 'w')
begin  
  # do something with file  
rescue  
  # handle exception  
rescue  
  # handle a different exception  
ensure  
  file.close  
  # executes every time  
end
```

The `retry` keyword redirects your program back to the `begin` statement. This allows your program to make another attempt to execute the code that **raised** an [[Exception]]. You may find `retry` useful when connecting to a remote server, for example. It's a good idea to set a limit on the number of times you want `retry` to execute:
```ruby
RETRY_LIMIT = 5
begin  
  attempts = attempts || 0  
  # do something  
rescue  
  attempts += 1  
  retry if attempts < RETRY_LIMIT  
end
```
## References
1. [ Getting Started With Ruby Exceptions (article)](https://launchschool.medium.com/getting-started-with-ruby-exceptions-d6318975b8d1)
2. [ Ruby Docs 3.2: Exception ](https://docs.ruby-lang.org/en/3.2/Exception.html)