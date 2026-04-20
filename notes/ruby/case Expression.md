Created: 2023-09-30 09:17

Case statements use the reserved words `case`, `when`, `else`, and `end`. Use it instead of [[if-else Expression]] when a single one of the [[Variable]] is to be compared against multiple values. 

The first `when` branch that matches is executed and all others are ignored. `then` keyword is optional. 

May have single-lined multiple conditions:
```ruby
case "2"
when /^1/, "2"
  puts "the string starts with one or is '2'"
end
```

[[Range]] can be used to augment comparison test. In the following example it is essentially calling `(range).include?(other_object)`:
```ruby
def get_grade(s1, s2, s3)
  result = (s1 + s2 + s3)/3

  case result
  when 90..100 then 'A'
  when 80..89  then 'B'
  when 70..79  then 'C'
  when 60..69  then 'D'
  else              'F'
  end
end
```
That's because behind the scenes, the `case` statement is using the `===` [[Method]] to compare each `when` clause with `result`. In this example, the `when` clauses contain only [[Range]]s, so `Range#===` is used for each clause.
## References
1. [Ruby Docs 3.2: syntax/control expressions/Case Expression](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-case+Expression)
2. [Ruby Style Guide: flow control/case vs if-else](https://rubystyle.guide/#case-vs-if-else)
3. [Intro to Programming with Ruby: Flow Control/Case Statement](https://launchschool.com/books/ruby/read/flow_control#casestatement)
4. [ RB101-119 Small Problems > Easy_9 > grade book ](https://launchschool.com/exercises/063fa805)
5. [ courses > RB120 > lesson 3 > 2. Equivalence ](https://launchschool.com/lessons/d2f05460/assignments/9cadd494)