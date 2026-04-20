Created: 2023-10-05 11:08

## Basics

* It is but a loose definition for grouped [[Object]]s structured as a single [[Object]] entity, i.e. data structured.
* We often want to perform [[Iteration]], [[Selection]] or [[Transformation]] ( [[Common Collection Methods Table]] is a good illustration) operations on collections using a [[Block]] argument to sweep through its elements. Using these 3 actions we can manipulate a collection nearly any way we need to.
* The [[Enumerable module]] is largely responsible for the functionalities of collections. [[Integer]]s, [[String]]s become **Enumerators**, which include [[Enumerable module]].
* A [[String]] is a single [[Object]], **not** a [[Collection]] of multiple [[Object]]s, though they can often be treated as such. The use of [[Method]]s that perform [[conversion to Collections]] is particularly common with [[String]]s.

---
## Notes

* Ruby only provides [[Shallow copy]] [[Method]]s and this brings particularly important implications to collections. [[Freeze]] will behave differently depending on what [[Shallow copy]] [[Method]] was used.
* Beware of the different mechanism and use-cases appropriate to [[map Method]] and [[each Method]] when trying to perform [[Transformation]] in [[Hash]]es. The latter provide a more convenient way to access the elements and use a [[Mutating method]], especially because the former's [[Return value]] is **always** an [[Array]], with the downside that it doesn't keep the original [[Hash]] unaltered:
```ruby
arr = [{a: 1}, {b: 2, c: 3}, {d: 4, e: 5, f: 6}] # mutates
arr.each { |hsh| hsh.each { |k,v| hsh[k] += 1 } } # => [{:a=>2}, {:b=>3, :c=>4}, {:d=>5, :e=>6, :f=>7}]

arr = [{a: 1}, {b: 2, c: 3}, {d: 4, e: 5, f: 6}] # doesn't mutate
arr.map do |hsh|
  incremented_hash = {}
  hsh.each do |key, value|
    incremented_hash[key] = value + 1
  end
  incremented_hash
end
# => [{:a=>2}, {:b=>3, :c=>4}, {:d=>5, :e=>6, :f=>7}]
```
* When [[Hash]]es are used in **SOME**  [[Collection]] [[Method call]]s, the [[Block parameter]] can be an [[Array]] of key-value pairs (this is not the case for `Hash#select!`):
```
>> { a: 1, b: 2, c: 3}.each { |x| p x }
=> [:a, 1]
=> [:b, 2]
=> [:c, 3]
```
## References
1. [Ruby Docs 3.2: Arrays](https://docs.ruby-lang.org/en/3.2/Array.html)
2. [Ruby Docs 3.2: Hash](https://docs.ruby-lang.org/en/3.2/Hash.html)
3. [Ruby Docs 3.2: Range](https://docs.ruby-lang.org/en/3.2/Range.html)
4. [Ruby Docs 3.2: Enumerable](https://docs.ruby-lang.org/en/3.2/Enumerable.html#module-Enumerable-label-Enumerable+in+Ruby+Classes)
5. [The Ruby Programming Language: Enumerable Objects](https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/)
6. [courses > RB110 > lesson 1 > 2. Collection Basics](https://launchschool.com/lessons/6a5eccc0/assignments/17756d47)
7. [courses > RB110 > lesson 1 > 7. Selection and Transformation](https://launchschool.com/lessons/6a5eccc0/assignments/d8fd867a)
8. [courses > RB110 > lesson 1 > 11. Practice Problems: Additional Practice > Problem 3](https://launchschool.com/lessons/6a5eccc0/assignments/3ae129af)