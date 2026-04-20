Created: 2023-10-19 13:23

## `Array#[]=`

Without [[Ruby's syntactical sugar]]:
```ruby
arr = %w(a b c)
arr.[]=(1, 'd')
arr # => ["a", "d", "c"]
```

* It is one of the [[Destructive method]] because it is mutating with respect to its caller, the [[Array]]:
```ruby
arr = ["a", "b", "c"]
arr.object_id # => 19
arr[0].object_id # => 75
arr[0] = "A"
arr[0].object_id # => 99
arr.object_id # => 19
```
* It is **not** mutating with respect to the RHS [[Object]] though, as the following code shows:
```ruby
a = 'hi' 
english_greetings = ['hello', a, 'good morning']
english_greetings[1] = 'hey' # => a still points to 'hi' 
```
* Unlike the [[Collection setter (String)]], it actually returns a reference to the element being assigned within the [[Array]]:
```ruby
array = %w(a b c)
(array[0] = 'd').<< 'ay'
p array # => ["day", "b", "c"] 
```
* Be aware that when using 2 arguments, the syntax is `Array#[start, length]= Object`:
```ruby
a = [:foo, 'bar', 2]
a[0, 2] = 'bat' # => "bat"
a # => ["bat", 2]
```
* If indexed position doesn't exist, it's created and all positions in between this, current one and the last existing are filled with `nil`.
## References
1. [Ruby Docs 3.2: Array](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-5B-5D-3D)