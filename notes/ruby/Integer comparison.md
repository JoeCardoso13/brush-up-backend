Created: 2023-11-03 10:48

[[Integer]]s use the [[Spaceship operator]] as illustrated:
```ruby
1 <=> 2              # => -1
1 <=> 1              # => 0
1 <=> 0              # => 1
1 <=> 'foo'          # => nil
```

(The [Numeric](https://docs.ruby-lang.org/en/3.2/Numeric.html) class have included the [[Spaceship operator]] however, in the case of [[Integer]] and [[Float]], these are overridden).
## References
1. [Ruby Docs 3.2: integers/Comparison](https://docs.ruby-lang.org/en/3.2/Integer.html#class-Integer-label-Comparing)