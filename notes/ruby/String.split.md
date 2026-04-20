Created: 2023-12-08 11:07

Its [[Return value]] is an [[Array]] of sub[[String]]s that are the result of separating the caller at each occurrence of the argument, which defaults to space if not provided:
```ruby
'abracadabra'.split('ab')  # => ["", "racad", "ra"]
```
It can take a [[Block]] (not common) which will iterate through each sub[[String]]:
```ruby
'abc def ghi'.split {|substring| p substring }
```
Output:
```
"abc"
"def"
"ghi"
```
## References
1. [ Ruby Docs 3.2: String / split ](https://docs.ruby-lang.org/en/3.2/String.html#method-i-split)