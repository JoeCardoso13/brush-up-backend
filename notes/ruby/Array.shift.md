Created: 2023-10-18 14:55

If no argument is given, it removes and returns the first argument:
```ruby
a = [:foo, 'bar', 2]
a.shift # => :foo
a # => ['bar', 2]
```
When positive Integer argument `n` is given, removes the first `n` elements; returns those elements in a new Array.
## References
1. [RB101: Lesson 2 Quiz > Question 8](https://launchschool.com/quizzes/60cdca5b)
2. [Ruby Docs 3.2: array/Shift](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-shift)