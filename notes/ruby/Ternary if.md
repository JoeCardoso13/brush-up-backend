Created: 2023-09-29 14:49

The following pieces of code are equivalent: 
```ruby
input_type = gets =~ /hello/i ? "greeting" : "other"
```

```ruby
input_type =
  if gets =~ /hello/i
    "greeting"
  else
    "other"
  end
```

A short, special, form of the [[if-else Expression]], not exactly equivalent. Better to be used when conditionally assigning [[Variable]]. [Ruby Style Guide](https://rubystyle.guide/) convention encourages its use. 

Be aware that, when your condition is guaranteed to return a [[Boolean]] (which should always be), it **does not make sense** to return `true` or `false`, like so:
```ruby
(a == b) ? true : false # => This doesn't make sense
```
## References
1. [Ruby Docs 3.2: syntax/Ternary if](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-Ternary+if)
2. [Ruby Style Guide > Ternary Operator vs if](https://rubystyle.guide/#ternary-operator)