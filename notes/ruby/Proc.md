Created: 2024-03-23 13:58

It is a way to use [[Closure]] to enclose a portion of code while [[Binding]] the surrounding artifacts. The enclosed "chunk of code" can then be passed around and executed through `Proc#call`.

"A `Proc` [[Object]] is an encapsulation of a [[Block]] of code, which can be stored in a [[Local variable]], passed to a [[Method]] or another [`Proc`](https://docs.ruby-lang.org/en/3.2/Proc.html), and can be called. [`Proc`](https://docs.ruby-lang.org/en/3.2/Proc.html) is an **essential** concept in Ruby and a core of its functional programming features."

It is the inner-mechanism through which Ruby transmit [[Block]]s to the code within [[Method definition]]s during [[Method call]]s. It can be made explicit by using **explicit** [[Block]] parameter (with `&`).

---
It is the mechanism through which Ruby allows the [[Block]] shortcut form:
```ruby
[1, 2, 3, 4, 5].map(&:to_s) # => ["1", "2", "3", "4", "5"]
```
This works for all the common [[Collection]] [[Method]]s, by the way:
```ruby
["hello", "world"].each(&:upcase!) # => ["HELLO", "WORLD"]
[1, 2, 3, 4, 5].select(&:odd?) # => [1, 3, 5]
[1, 2, 3, 4, 5].select(&:odd?).any?(&:even?) # => false
```
More generally, these are equivalent to:
```
(&:to_s) => { |x| x.to_s }
```
So much so that the following code throws **no** [[Exception]]:
```ruby
'abc'.upcase(&:to_i) # => "ABC"
```

What happens behind the scenes, is that the [[Symbol]] `:method_name` is turned into a Proc, using `#to_proc`, then the Proc is turned into a [[Block]] by prepending it with `&`. For example, to use the **Proc** to produce the [[Block]] argument to the [[Sorting method]] we may do as follows:
```ruby
array = 5, 3, 76, 3, 7, 4, 8
comparator = proc { |a, b| b <=> a }
array.sort(&comparator)
```
So the following code:
```ruby
def my_method
  yield(2)
end

my_method(&:to_s) # => "2"
```
Is equivalent to:
```ruby
def my_method
  yield(2)
end

a_proc = :to_s.to_proc # explicitly call to_proc on the symbol
my_method(&a_proc) # convert Proc into block, then pass block in. Returns "2"
```
## References
1. [ Ruby Docs 3.2: Proc ](https://docs.ruby-lang.org/en/3.2/Proc.html)