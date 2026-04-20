Created: 2023-10-19 14:22

==> A.K.A. Enumerable.find_all, Enumerable.filter

It executes the given [[Block]] once for each element in the [[Collection]] and evaluates it in terms of **truthiness** ([[Truthy]] or [[Falsy]] [[Return value]] of last [[Expression]]). It returns a **new** [[Collection]] containing all of the elements where the [[Block]] was evaluated as [[Truthy]] (in the case of [[Hash]] an element is a key-value pair).

```ruby
{ "a" => 100, "b" => 200, "c" => 300 }.select do |key, value|
value < 200
end # => returns { "a" => 100}
```

Note that the [[Enumerable module]] defines a select method (with the aliases above mentioned) where the [[Return value]] is an [[Array]]. However, being so common, this method is usually overridden in most [[Collection]] classes. That is the case for [[Hash]]es, and it leads to a nuance that `Hash#select` returns a [[Hash]] whereas `Hash#find_all` returns a nested [[Array]].  
## References
1. [the SPOT wiki > Assignment_preparation.pdf](https://fine-ocean-68c.notion.site/SPOT-Wiki-b58ff38ab84440bdb96797e59ee5fd34)
2. [courses > RB110 > Lesson 1 > 8. Each, Select and Map Methods](https://launchschool.com/lessons/6a5eccc0/assignments/da1f87fe)