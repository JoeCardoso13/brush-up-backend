Created: 2023-09-28 10:26

They're used to map unique keys to values. Hash [[Literal]] are created using key-value pairs, written like: `key => value` between curly braces. They can also be created with JSON-like syntax, like so: `h = {foo: 0, bar: 1, baz: 2}`, which is more common (but then its keys will necessarily be [[Symbol]]). Although in newer versions of Ruby they are ordered by creation, they're not typically used when element ordering matters. 

* When used in a [[Collection]] [[Method call]], the [[Block parameter]] **can** be [[Array]] of key-value pairs:
```
>> { a: 1, b: 2, c: 3}.each { |x| p x }
=> [:a, 1]
=> [:b, 2]
=> [:c, 3]
```
Note the implication here:
```
{foo: 0, bar: 1, baz: 2}.any?(Array) # => true
{foo: 0, bar: 1, baz: 2}.any?(Hash)  # => false
```
* When using key-value pairs of hashes in [[Block]] [[Iteration]]s, be aware that the parenthesis are **not** optional when there are additional [[Block parameter]]s:
```ruby
# This does NOT work if block parameter is simply |k, v, arr| 
munsters.each_with_object([]) { |(k, v), arr| arr << v['age'] if v['gender'] == 'male' }.sum
```
* Repeating keys overrides the first value:
```
> hsh = {a: 100, b: 200, c: 300, a: 400}
(irb):1: warning: key :a is duplicated and overwritten on line 1
 => {:b=>200, :c=>300, :a=>400}
```
* Hash values can be fetched from the context by the name of the key:
```ruby
x = 100
y = 200
h = { x:, y: }
#=> {:x=>100, :y=>200}
```
* You may omit the curly braces `{}` if passing a hash as **the last** argument in a [[Method call]] (common convention for Rails developers). 
## References
1. [Intro to Programming with Ruby: The Basics/Hashes](https://launchschool.com/books/ruby/read/basics#hashes)
2. [Ruby Docs 3.2: Hash](https://docs.ruby-lang.org/en/3.2/Hash.html)
3. [Ruby Docs 3.2: syntax/literals/Hash Literals](https://docs.ruby-lang.org/en/3.2/syntax/literals_rdoc.html#label-Hash+Literals)