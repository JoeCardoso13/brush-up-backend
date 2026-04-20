Created: 2023-10-12 14:57

## `Array#[]`

Without [[Ruby's syntactical sugar]]:
```ruby
arr = %w(a b c)
arr.[](1) # => 'b'
```

It returns an element from the [[Array]] [[Object]] caller (`self`). 

It returns a reference to existing [[Object]], does **not** create new [[Object]] (thence [[Object passing]] may take place). **Different** from [[Collection getter (String)]] in this regard:
```
3.2.2 :027 > a = %w(a b c)
 => ["a", "b", "c"]
3.2.2 :028 > a[1].object_id
 => 194060
3.2.2 :029 > a[1].object_id
 => 194060
3.2.2 :030 > a[1].object_id
 => 194060
```

When called with 2 [[Integer]] arguments, or a [[Range]], its [[Return value]] is a new [[Array]]:
```ruby
arr = [1, 'two', :three, '4']
id1 = arr.slice(3, 1).object_id # => ["4"].object_id
id2 = arr.slice(3..3).object_id # => ["4"].object_id
puts id1 == id2 # => false
```

It returns `nil` if index is out of bounds. Different from `Array#fetch` in this regard:
```ruby
arr = [3, 'd', nil]
arr[2] # => nil
arr[3] # => nil
arr.fetch(2) # => nil
arr.fetch(3) # => IndexError: index 3 outside of array bounds: -3...3
```
## References
1. [Ruby Docs 3.2: Array](https://docs.ruby-lang.org/en/3.2/Array.html#method-i-5B-5D)
2. [courses > RB110 > Lesson 1 > 2. Collection Basics](https://launchschool.com/lessons/6a5eccc0/assignments/17756d47)