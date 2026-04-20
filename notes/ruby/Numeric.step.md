Created: 2023-12-08 08:43

Generates a sequence of numbers. If a with a [[Block]] is given, traverses the sequence.

From the Core and Standard Library [[Class]]es, [[Integer]], [[Float]], and Rational use this implementation.

A quick example:
```ruby
  squares = []
  1.step(by: 2, to: 10) {|i| squares.push(i*i) }
  squares # => [1, 9, 25, 49, 81]
```

The generated sequence:
- Begins with caller.
- Continues at intervals of **step** (which may not be zero).
- Ends with the last number that is within or equal to **limit** (that is, less than or equal to **limit** if **step** is positive, greater than or equal to **limit** if **step** is negative. If **limit** is not given, the sequence is of infinite length).

If a [[Block]] is given, calls the [[Block]] with each number in the sequence. Its [[Return value]] is the caller. If no block is given, returns an [[Enumerator]]. 

<b>Keyword Arguments</b>

With keyword arguments **by** and **to**, their values (or defaults) determine the **step** and **limit**:
```ruby
  # Both keywords given.
  squares = []
  4.step(by: 2, to: 10) {|i| squares.push(i*i) }    # => 4
  squares # => [16, 36, 64, 100]
  cubes = []
  3.step(by: -1.5, to: -3) {|i| cubes.push(i*i*i) } # => 3
  cubes   # => [27.0, 3.375, 0.0, -3.375, -27.0]
  squares = []
  1.2.step(by: 0.2, to: 2.0) {|f| squares.push(f*f) }
  squares # => [1.44, 1.9599999999999997, 2.5600000000000005, 3.24, 4.0]

  squares = []
  Rational(6/5).step(by: 0.2, to: 2.0) {|r| squares.push(r*r) }
  squares # => [1.0, 1.44, 1.9599999999997, 2.56000000000005, 3.24, 4.0]

  # Only keyword to given.
  squares = []
  4.step(to: 10) {|i| squares.push(i*i) }           # => 4
  squares # => [16, 25, 36, 49, 64, 81, 100]
  # Only by given.

  # Only keyword by given
  squares = []
  4.step(by:2) {|i| squares.push(i*i); break if i > 10 }
  squares # => [16, 36, 64, 100, 144]

  # No block given.
  e = 3.step(by: -1.5, to: -3) # => (3.step(by: -1.5, to: -3))
  e.class                      # => Enumerator::ArithmeticSequence
```
Both colons and equal signs are accepted for assigning keywords; **by** defaults to 1 and **to** defaults to `nil`. 

<b>Positional Arguments</b>

With optional positional arguments **limit** and **step**, i.e. when keywords are not used, the order is **to** 1st, then **by**:
```ruby
  squares = []
  4.step(10, 2) {|i| squares.push(i*i) }    # => 4
  squares # => [16, 36, 64, 100]
  squares = []
  4.step(10) {|i| squares.push(i*i) }
  squares # => [16, 25, 36, 49, 64, 81, 100]
  squares = []
  4.step {|i| squares.push(i*i); break if i > 10 }  # => nil
  squares # => [16, 25, 36, 49, 64, 81, 100, 121]
```
## References
1. [ Ruby Docs 3.2: Numeric / step ](https://docs.ruby-lang.org/en/3.2/Numeric.html#method-i-step)