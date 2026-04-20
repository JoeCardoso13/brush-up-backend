Created: 2023-10-12 14:46

=> Alias for [[String.slice]]
## `String#[]`

Without [[Ruby's syntactical sugar]]:
```ruby
str = 'abc'
str.[](1) # => 'b'
```

* It is fundamentally **different** from [[Collection getter (Array)]] and [[Collection getter (Hash)]] in that its [[Return value]] is a new [[Object]]. This is **the reason why** [[String]]s are not [[Collection]]s:
```
3.2.2 :014 > a = 'abc'
 => "abc"
3.2.2 :015 > a[1].object_id
 => 88860
3.2.2 :016 > a[1].object_id
 => 92000
3.2.2 :017 > a[1].object_id
 => 95140
```
* Be very careful when using it in [[Method chain]] because its [[Return value]] is a new string:
```ruby
def unexpected(str)
  str[1].downcase!
  puts str
end
word = "HELLO"
unexpected(word)
```
  Mutating its [[Return value]] won't affect the original [[String]]. 

* If needing to substitute **more than one** value of [[String]], be aware that the second argument does **not** refer to an index. Syntax is `string[start, length]`. You can use [[Range]] to do that though:
```
 > 'abcdefg'[0..-3]
=> "abcde"
```
## References
1. [Ruby Docs 3.2: Strings](https://docs.ruby-lang.org/en/3.2/String.html#method-i-5B-5D)
2. [ RB101-119 > Easy_4 > convert string to signed number](https://launchschool.com/exercises/52e5f20f)