Created: 2023-10-07 11:52

**It is how** different [[Local variable]] can point to the same [[Object]], i.e. show behavior like [[Variables as pointers]]. It can happen in 4 ways: 

1. It can happen when both sides of an [[Assignment]] [[Expression]], i.e. the left-hand-side and right-hand-side of `=`, are [[Local variable]], and therefore are references to their respective [[Object]], like in `a = b` (see [[Variables as pointers]]).

2. Happens when [[Method]] return an existing [[Object]]. Most commonly, it happens when the [[Return value]] of a [[Method call]] on the right-hand-side of an [[Assignment]] [[Expression]] is 'self'. In the example below it happens on `line 2`:
```ruby 
a = 'abc'
b = a.upcase!
b << " This will affect 'a' as well"
p a
p b
```
Outputs:
```
>> "ABC This will affect 'a' as well"
>> "ABC This will affect 'a' as well"
```

3. It is how the arguments used in an [[Method call]] are passed to the parameters of the [[Method definition]], through the [[Pass by copy of reference]] strategy. The [[Object ID]] here is used to identify a specific [[Object]], i.e. a unique place in memory:
```ruby
def my_method(b)
  b.object_id
end
a = 'abc'
puts a.object_id == my_method(a)
```
Outputs:
```
>> true
```

4. Finally, it is how the [[Block parameter]] is assigned to the elements of the [[Collection]] caller during an [[Iteration]] in a [[Collection]] [[Method call]]:
```ruby
arr = %w(a b c)
params_id = []
arr.each do |n|
  params_id << n.object_id
end
p [arr[0].object_id, arr[1].object_id, arr[2].object_id] == params_id
```
Outputs:
```
>> true
```
## References
1. [Mutating and Non-mutating Methods in Ruby (articles Part 2)](https://launchschool.medium.com/ruby-objects-mutating-and-non-mutating-methods-78023d849a5f)