Created: 2023-09-30 09:46

* Use `break` to leave a [[Block]] early.
* Use `break` to terminate [[Control Expression]] **iterations** early.
* `break` accepts a value that supplies the result of the expression it is breaking out from:
```ruby
result = [1, 2, 3].each do |value|
  break value * 2 if value.even?
end
p result # prints 4
```
* `break` is for **iterations** - whereas happening in [[Block]]s or [[Control Expression]]s - what `return` is for [[Method invocation]]. ([[Return vs break]])
* If nested, use one `break` for each [[Block]] or [[Control Expression]].
## References
1. [Ruby Docs 3.2: syntax/Control Expressions](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-break+Statement)