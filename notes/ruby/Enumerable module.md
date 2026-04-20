Created: 2023-10-15 12:03

[[Array]], [[Hash]] and [[Range]] classes include the enumerable module. *This is probably why [[Collection getter (Array)]] and [[Collection getter (Hash)]] are so different from [[Collection getter (String)]].* 

Other classes that do so are:
* ARGF
* Dir
* [[Enumerator]] (probably why [[Integer]] [[Iteration]] [[Method]]s return it when no [[Block]] argument is given)
* IO
* Struct
Whereas "ENV" extends it.

Virtually all [[Method]]s in Enumerable have [[each Method]] in the including class for iterations:
- [[Hash]] [[each Method]] yields key-value pairs as a 2-element Array.
- For the other classes above, [[each Method]] yields [[Object]]s from the [[Collection]].

---

To use module Enumerable in a collection class:
1) Include it:
```ruby
include Enumerable
```

2) Implement method `#each` which must yield successive elements of the collection. The method will be called by almost any Enumerable method.
```ruby
class Foo
  include Enumerable
  def each
    yield 1
    yield 1, 2
    yield
  end
end
Foo.new.each_entry{ |element| p element }
```
Output:
```
1
[1, 2]
nil
```
## References
1. [Ruby docs 3.2: enumerable](https://docs.ruby-lang.org/en/3.2/Enumerable.html)