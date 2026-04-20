Created: 2023-10-15 11:55

==> A.K.A. Enumerable.reduce

Accessible from the [[Enumerable module]]. Returns an [[Object]] formed from operands via either:
- A method named by [[Symbol]].
- A [[Block]] to which each operand is passed.

With method-name argument [[Symbol]], combines operands using the method:
```ruby
# Sum, without initial_operand.
(1..4).inject(:+)     # => 10 (equivalent to #sum method)
# Sum, with initial_operand.
%w[a b c].inject(['x'], :push)     # => ["x", "a", "b", "c"]
```
Note that `Array#sum` is **almost** contained here as a special (the simplest) case **but** when [[Method invocation]] is by an **empty** [[Collection]], [[Return value]] is 0, **not** `nil`!

---
With a [[Block]] argument, it's a lot more complex. Let's first consider calling it without **initial operand**:
```
> (1..13).inject { |sum, n| puts "First block parameter: #{sum}, second: #{n}"; sum + n }
First block parameter: 1, second: 2
First block parameter: 3, second: 3
First block parameter: 6, second: 4
First block parameter: 10, second: 5
First block parameter: 15, second: 6
First block parameter: 21, second: 7
First block parameter: 28, second: 8
First block parameter: 36, second: 9
First block parameter: 45, second: 10
First block parameter: 55, second: 11
First block parameter: 66, second: 12
First block parameter: 78, second: 13
 => 91
```
It iterates through the [[Block]] **1 less times** the number of elements in the [[Collection]] caller. That's because the first [[Block parameter]] takes the first [[Collection]] element in the first iteration. Thence this parameter takes the [[Return value]] of the [[Block]] for each [[Iteration]] and, in the last [[Iteration]], it provides the [[Return value]] for the [[Method call]] itself. 

When using an **initial operand**, though, the number of [[Iteration]]s corresponds, as commonly, to the number of elements in the [[Collection]] caller:
```
> (1..13).inject(0) { |sum, n| puts "First block parameter: #{sum}, second: #{n}"; sum + n }
First block parameter: 0, second: 1
First block parameter: 1, second: 2
First block parameter: 3, second: 3
First block parameter: 6, second: 4
First block parameter: 10, second: 5
First block parameter: 15, second: 6
First block parameter: 21, second: 7
First block parameter: 28, second: 8
First block parameter: 36, second: 9
First block parameter: 45, second: 10
First block parameter: 55, second: 11
First block parameter: 66, second: 12
First block parameter: 78, second: 13
 => 91
```
In the first [[Iteration]] the first [[Block parameter]] now gets assigned to the **initial operand**. The second [[Block parameter]] this times takes all the elements of the [[Collection]] caller. From the second [[Iteration]] afterwards, the first [[Block parameter]] accumulates the [[Return value]]s of each [[Block]] [[Iteration]] and, by the end, provides for the [[Return value]] of the [[Method call]] itself.

If the [[Return value]] ever gets evaluated as `nil`, it will be assigned to the next [[Iteration]] of the [[Block parameter]] as usual, hence breaking the code if being used as shown above. This behavior is similar to [[map Method]] however significantly different from [[Enumerable.each_with_object]]:
```
[1, 2, 3].reduce do |acc, num|
  acc + num if num.odd?
end

# => NoMethodError: undefined method `+' for nil:NilClass
```
## References
1. [Ruby Docs 3.2: enumerable/Inject](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-inject)
2. [RB101-RB109 - Small Problems > Easy 2 > Sum or Product of Consecutive Integers](https://launchschool.com/exercises/b720efd9)
3. [ courses > RB130 > lesson 1: blocks > build a 'reduce' method ](https://launchschool.com/lessons/c0400a9c/assignments/c1edc867)