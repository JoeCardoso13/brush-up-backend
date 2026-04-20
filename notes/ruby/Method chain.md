Created: 2023-09-29 12:29

* Because we know for certain that every [[Method call]] returns something (a [[Return value]]), we can chain methods together. 
* Ruby will compute a method chain from left to right:
```ruby
def interleave(array1, array2)
  result = []
  array1.each_with_index do |element, index|
    result << element << array2[index]
  end
  result
end

interleave([1, 2, 3], ['a', 'b', 'c']) == [1, 'a', 2, 'b', 3, 'c'] # => true
```
* [[Collection]]s ([[String]] included) can be chained nicely, and interchangeably: 
```ruby
str = 'abcdefghi'
str[2, 3][0] # => "c"
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
arr[2, 3][0] # => "c"
hsh = { 'fruit' => 'apple', 'vegetable' => 'carrot' }
hsh['fruit'][0] # => "a"
```

Under the [[OOP]] perspective, each [[Object]] is an instance from its [[Class]] and by calling the pre-defined [[Instance method]]s sequentially, upon each [[Return value]] which itself is another [[Object]], we are using **collaborator objects**.
## References
1. [Ruby Docs 3.2: syntax/calling methods/Chaining Method Calls](https://docs.ruby-lang.org/en/3.2/syntax/calling_methods_rdoc.html#label-Chaining+Method+Calls)
2. [Intro to Programming with Ruby: Methods/Chaining Methods](https://launchschool.com/books/ruby/read/methods#chainingmethods)
3. [courses > RB110 > Lesson 1 > 2. Collection Basics](https://launchschool.com/lessons/6a5eccc0/assignments/17756d47)
4. [ courses > RB120 > lesson 2 > 9. lecture: collaborator objects ](https://launchschool.com/lessons/dfff5f6b/assignments/4228f149)