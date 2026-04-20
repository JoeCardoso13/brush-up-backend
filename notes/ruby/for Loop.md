Created: 2023-09-30 09:38

The `for/in` loop calls the [[each Method]] of the specified object, but it **does not** create a new [[Variable Scope]], since it is one of the [[Control Expression]]. It looks like this: 
```ruby
for var in collection do
  body
end
```
The `var` is a [[Local variable]] or a comma separated list of [[Local variable]]s, whereas [[Collection]] is any object that has the [[each Method]]. The `do` is optional. The [[Return value]] is the [[Collection]] caller itself, just like the [[each Method]].

If `var` does not exist, it will have its [[Initialization]]. It will thence be available in the current [[Variable Scope]] pointing to the [[Object]] corresponding to its last [[Re-assignment]], i.e. last element from `collection`, unless `collection` is empty. 

The `for/in` loop is rarely used in modern ruby programs. Ruby Style Guide recommends **avoidance**.
## References
1. [Ruby Docs 3.2: syntax/control expressions/For Loop](https://docs.ruby-lang.org/en/3.2/syntax/control_expressions_rdoc.html#label-for+Loop)
2. [The Ruby Programming Language: 5. Statements and Control Structures](https://www.oreilly.com/library/view/the-ruby-programming/9780596516178/)
3. [Intro to Programming with Ruby: Loops & Iterators/For Loops](https://launchschool.com/books/ruby/read/loops_iterators#forloops)
4. [Ruby Style Guide: no-for-loops](https://rubystyle.guide/#no-for-loops)