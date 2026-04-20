Created: 2023-09-29 11:14

## Basics

* [[Fake operators]] is a list to distinguish the actual operators, in Ruby, from the [[Method]]s that are disguised as operators through **Ruby's syntactical sugar**.
* Parenthesis are optional for [[Method invocation]]s in Ruby. This is why, in Ruby, a typical error message is "*undefined variable or method*" . When [[Local variable]]s and [[Method]]s have the same name, parenthesis can be used to avoid ambiguity but, if not, Ruby uses the variable first. Parenthesis are also optional in a [[Method definition]]. 
* The `return` reserved word can be omitted of a [[Method definition]]. 
* [[Collection setters]] are actually [[Method]]s, not [[Assignment]]s.
* [[Exception raising]] got a prettier option:
```ruby
raise TypeError.new("Something went wrong!")
raise TypeError, "Something went wrong!"
```

---
## Multiple assignment

* With `*` (asteristik) Ruby creates [[Array]] automatically.  Here with parameters in a [[Method definition]]:
```ruby 
def display_results(*results, lang)
	# body
end
```
* Also, using `,` (comma) is an easier syntax for [[Array]] creation. 
```ruby
return monthly_rate, months, monthly_payment, total_paid
```

The 2 syntax above can lead to more readable, compact code that also facilitates compliance with [Ruby Style Guide](https://rubystyle.guide/) in order not to upset Rubocop. 

[[Parallel assignment]] is a particularly well suited use-case for it.

---
## Intermediate

* When the last argument in a method call is of [[Hash]] class, the curly braces may be omitted:
```ruby
some_method(foo: 0, bar: 1, baz: 2) # => {:foo=>0, :bar=>1, :baz=>2}
```
* For simple iteration [[Block]]s you may use:
```
something.map(&:to_i)
```

## References
1. [LS live session](https://youtu.be/SYkDoRdJjCo "Share link")
2. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods) 
3. [Ruby Docs 3.2: syntax/methods/Arguments](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Arguments)
4. [Ruby Docs 3.2: Hash](https://docs.ruby-lang.org/en/3.2/Hash.html)
5. [courses > RB101 > lesson 2 > 18. Variable Scope](https://launchschool.com/lessons/8a39abff/assignments/e3cd8bb9)
6. [Ruby Docs 3.2: syntax/methods/Array/Hash Argument](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Array-2FHash+Argument)
7. [ RB101-119 Small Problems > Easy_5 > list of digits ](https://launchschool.com/exercises/f2f0431c)