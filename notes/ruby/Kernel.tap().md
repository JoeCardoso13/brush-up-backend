Created: 2023-10-05 18:13

It is primarily used to "tap into" a [[Method chain]]. The calling object yields itself to the [[Block]] and then returns itself. To illustrate:
```ruby
(1..10)                  .tap {|x| puts "original: #{x}" }
  .to_a                  .tap {|x| puts "array:    #{x}" }
  .select {|x| x.even? } .tap {|x| puts "evens:    #{x}" }
  .map {|x| x*x }        .tap {|x| puts "squares:  #{x}" }
```
Will output:
```
original: 1..10
array:    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens:    [2, 4, 6, 8, 10]
squares:  [4, 16, 36, 64, 100]
```
## References
1. [Ruby Docs 3.2: kernel/tap](https://docs.ruby-lang.org/en/3.2/Kernel.html#method-i-tap)
2. [courses > RB101 > lesson 2 > Precedence](https://docs.ruby-lang.org/en/3.2/Kernel.html#method-i-tap)