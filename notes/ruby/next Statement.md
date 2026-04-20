Created: 2023-09-30 09:56

* You can use `next` to skip the rest of the current [[iteration]]:
```ruby
result = [1, 2, 3].map do |value|
  next if value.even?
  value * 2
end
p result # prints [2, nil, 6]
```
* And it does accept an argument that can be used as result of current [[iteration]]:
```ruby
result = [1, 2, 3].map do |value|
  next value if value.even?
  value * 2
end
p result # prints [2, 2, 6]
```
## References
1. [Ruby docs 3.2: syntax/control expressions/next Statement](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-next+Statement)