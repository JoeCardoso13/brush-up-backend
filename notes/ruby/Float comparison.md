Created: 2023-11-03 10:53

[[Float]]s use the [[Spaceship operator]] as illustrated:
```ruby
2.0 <=> 2              # => 0
2.0 <=> 2.0            # => 0
2.0 <=> 1.9            # => 1
2.0 <=> 2.1            # => -1
2.0 <=> 'foo'          # => nil
```

(the [Numeric](https://docs.ruby-lang.org/en/3.2/Numeric.html) class have included the [[Spaceship operator]] however, in the case of [[Integer]] and [[Float]], these are overridden).
## References
1. [Ruby Docs 3.2: floats/Comparison](https://docs.ruby-lang.org/en/3.2/Float.html#class-Float-label-Comparing)