Created: 2023-09-29 13:32

The following piece of code:
```ruby
def first
  puts "first method"
end

def second
  first
  puts "second method"
end

second
```

Will generate the following call stacks when executed (left to right):

| **call stack** | **call stack** | **call stack** | **call stack** | **call stack** | **call stack** | **call stack** | **call stack** | **call stack** | **call stack** |
| - | - | - | - | - | - | - | - | - | - |
| - | - | - | puts | - | - | - | - | - | - |
| - | - | first | first: line 2 | first: line 2 | - | puts | - | - | - |
| - | second | second: line 6 | second: line 6 | second: line 6 | second: line 6 | second: line 7 | second: line 7 | - | - |
| main | main: line 10 | main: line 10 | main: line 10 | main: line 10 | main: line 10 | main: line 10 | main: line 10 | main: line 10 | - |
****
And that is abstracting away the further subsequent calls within the `Kernel#puts` method call. 

The call stack is essential when determining the [[Variable Scope]]. 
## References
1. [Intro to Programming with Ruby: Methods/Call Stack](https://launchschool.com/books/ruby/read/methods#callstack)