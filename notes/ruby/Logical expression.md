Created: 2023-10-04 11:41

Logical operators `||` (or) and `&&` (and) use short-circuit evaluation. This means they will **stop** evaluating an [[Expression]], from left-to-right, once the result is guaranteed. 

When concatenating and nesting logical expressions, the order of [[Precedence]] will be paramount. 

Unlike in a [[Conditional expression]], these expressions may return [[Falsy]] and [[Truthy]] values too, i.e. they will **not** necessarily evaluate to/result in a [[Boolean]].

Their [[Return value]] is the value of operand evaluated last:
```ruby
irb :001 > 3 || 'foo' # last evaluated operand is 3 
=> 3 
irb :002 > 'foo' || 3 # last evaluated operand is 'foo' 
=> 'foo' 
irb :003 > nil || 'foo' # last evaluated operand is 'foo' 
=> 'foo' 
irb :004 > nil && 'foo' # last evaluated operand is nil 
=> nil 
irb :005 > 3 && 'foo' # last evaluated operand is 'foo' 
=> 'foo' 
irb :006 > 'foo' && 3 # last evaluated operand is 3 
=> 3
```

Be aware the following equivalency:
```ruby
# This logical expression:
last_login < 60 && subscribed_to_list
# Is equivalent to this logical expression:
!(last_login > 59 || !subscribed_to_list)
```
That is, if you have 2 conditions, and both of them need to be true, that's the same as neither of them being allowed to be false. So, if either the first, or the second condition, is false, your logical assessment evaluates to false.
## References
1. [Intro to Programming with Ruby: Flow Control/True and False](https://launchschool.com/books/ruby/read/flow_control#trueandfalse)