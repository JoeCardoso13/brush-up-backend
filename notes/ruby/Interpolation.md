Created: 2023-09-27 10:28

The following syntax defines [[String]] interpolation:
```ruby
"Lorem ipsum #{code here} dolor sit #{more code} amet."
```
[Ruby Style Guide](https://rubystyle.guide/#string-interpolation) favors [[String]] interpolation over [[String concatenation]].

If need to use [[Backslash character]] you can opt, instead, for `%()`:
```ruby
> str = %( I'm about to "quote" you )
 => " I'm about to \"quote\" you "
```

Ruby is using the `to_s` method behind the scenes.

[[Kernel.format]] is a more powerful way of doing just that.
## References
1. [Intro to Programming with Ruby: The Basics/Strings](https://launchschool.com/books/ruby/read/basics#strings)
2. [Ruby Style Guide: String Interpolation](https://rubystyle.guide/#string-interpolation)
3. [Intro to Programming with Ruby: Arrays/to_s](https://launchschool.com/books/ruby/read/arrays#to_s)