Created: 2024-01-19 10:47

It is important to understand that [[Exception]]s you **raise** manually in your program can be handled ([[Exception handling]]) in the same manner as [[Exception]]s Ruby **raises** automatically. Example:
```ruby
def validate_age(age)  
  raise("invalid age") unless (0..105).include?(age)  
end

begin  
  validate_age(age)  
rescue RuntimeError => e  
  puts e.message #=> "invalid age"  
end
```
You can also build custom-made [[Exception]] [[Class]]es while using [[Inheritance]] to keep all the useful built-in functionality. The above code can be slightly modified as follows:
```ruby
class ValidateAgeError < StandardError; end

def validate_age(age)  
  raise ValidateAgeError, "invalid age" unless (0..105).include?(age)  
end
begin  
  validate_age(age)  
rescue ValidateAgeError => e  
  # take action  
end
```

A small dose of [[Ruby's syntactical sugar]] is available when using `raise` statement.

If you do not specify what type of [[Exception]] to raise, Ruby will default to `RuntimeError` (a subclass of `StandardError`).
## References
1. [ Getting Started With Ruby Exceptions (article)](https://launchschool.medium.com/getting-started-with-ruby-exceptions-d6318975b8d1)
2. [ Ruby Docs 3.2: Exception ](https://docs.ruby-lang.org/en/3.2/Exception.html)