Created: 2023-09-30 09:09

The keywords `if` and `unless` can also be used in a [[Modifier statement]]. When used as a modifier the left-hand side is the “then” statement (from [[if-else Expression]]) and the right-hand side is the “test” [[Expression]]:
```ruby
a = 0
a += 1 if a.zero?
p a

a = 0
a += 1 unless a.zero?
p a
```

```
=> 1
=> 0
```
## References
1. [Ruby Docs 3.2: syntax/control expressions/Modifier Statements](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-Modifier+Statements)
2. [Ruby Docs 3.2: syntax/control expressions/Modifier if and unless](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-Modifier+if+and+unless)