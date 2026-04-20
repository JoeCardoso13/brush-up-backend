Created: 2023-10-05 10:46

==> A.K.A. Enumerable.collect

Returns a **new [[Array]]** filled with the [[Block]]'s [[Return value]] for each [[Iteration]], so that the *resulting [[Array]] will always have the same number of elements as the [[Collection]] caller*. The [[Block parameter]]s are the elements in the [[Collection]]. So, for example:
```ruby
[1, 2, 3].map do |num|
puts num 
end # => [nil, nil, nil]
```

It is particularly suitable for type **conversions**. A big [[case Expression]] can be turned into a [[Hash]] (as in [RB101-119 Small problems > Easy 4 > convert string to number](https://launchschool.com/exercises/192719a5)). The [[Ruby's syntactical sugar]] shortened version is not coincidentally made for type **conversions**.

It provides built-in [[Array]] decomposition:
```
> arr = [["apples", 3], ["orange", 1], ["bananas", 2]]
> arr.map { |fruit, quantity| "#{quantity} #{fruit}" }
=> ["3 apples", "1 orange", "2 bananas"]
```

If you are modifying some elements of the caller, but keeping others, it might be neat to use [[next Statement]] in the map [[Block]] like this:
```
Collection.map { |element| next element if condition; ... }
```
Or using the [[Enumerable.each_with_object]] since it doesn't return [[Falsy]] [[Block]]s.

If you have an [[each Method]] as the last [[Expression]] in a map [[Block]], then you don't need to check further to know its [[Return value]]:
```ruby
[[[1], [2], [3], [4]], [['a'], ['b'], ['c']]].map do |element1|
  element1.each do |element2|
    element2.partition do |element3|
      element3.size > 0
    end
  end
end
# => [[[1], [2], [3], [4]], [["a"], ["b"], ["c"]]]
```
## References
1. [Intro to Programming with Ruby: Arrays/Each vs Map](https://launchschool.com/books/ruby/read/arrays#eachvsmap)
2. [courses > RB110 > Lesson 1 > 8. Each, Select and Map Methods](https://launchschool.com/lessons/6a5eccc0/assignments/da1f87fe)
3. [RB101-119 Small Problems > Easy 4 > running totals](https://launchschool.com/exercises/ba434183)
4. [RB101-119 Small problems > Easy 4 > convert string to number](https://launchschool.com/exercises/192719a5)
5. [ courses > RB110 > lesson 2 > 4. Working with Blocks ](https://launchschool.com/lessons/fa1f5e7e/assignments/084fe222)