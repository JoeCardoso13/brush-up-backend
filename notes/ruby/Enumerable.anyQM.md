Created: 2023-12-08 10:27

[[Return value]] is `true` or `false` depending if any element of the [[Collection]] caller meets given criterion. 

With no argument and no [[Block]], returns whether any element is [[Truthy]]:
```ruby
(1..4).any?          # => true
%w[a b c d].any?     # => true
[1, false, nil].any? # => true
[].any?              # => false
```
With argument but no [[Block]], returns whether any element satisfies ([[Tripple equal]]) `===` [[Comparable module]]:
```ruby
[nil, false, 0].any?(Integer)        # => true
[nil, false, 0].any?(Numeric)        # => true
[nil, false, 0].any?(Float)          # => false
%w[bar baz bat bam].any?(/m/)        # => true
%w[bar baz bat bam].any?(/foo/)      # => false
%w[bar baz bat bam].any?('ba')       # => false
{foo: 0, bar: 1, baz: 2}.any?(Array) # => true
{foo: 0, bar: 1, baz: 2}.any?(Hash)  # => false
[].any?(Integer)                     # => false
```
With a [[Block]] given, returns whether it gets evaluated as [[Truthy]] for any of the elements of the [[Collection]] caller:
```ruby
(1..4).any? {|element| element < 2 }                    # => true
(1..4).any? {|element| element < 1 }                    # => false
{foo: 0, bar: 1, baz: 2}.any? {|key, value| value < 1 } # => true
{foo: 0, bar: 1, baz: 2}.any? {|key, value| value < 0 } # => false
```

`Enumerable#all?` does pretty much the same thing except it checks for every single (all) elements in the [[Collection]].
## References
1. [ Ruby Docs 3.2: Enumerable / anyQM ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-any-3F)
2. [ courses > RB110 > lesson 1 > Discussions > How do these... ](https://launchschool.com/posts/fff43a91)