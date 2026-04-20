Created: 2023-10-24 13:27

Removes and returns the substring of `self` specified by the arguments. Difference from [[String.slice]] ([[Collection getter (String)]]) in that it is on the [[List of destructive methods]], i.e. it mutates its caller.

```ruby
string = "This is a string"
string.slice!(2)        #=> "i"
string.slice!(3..6)     #=> " is "
string.slice!(/s.*t/)   #=> "sa st"
string.slice!("r")      #=> "r"
string                  #=> "Thing"
```
## References
1. [Ruby Docs 3.2: string/slice!](https://docs.ruby-lang.org/en/3.2/String.html#method-i-slice-21)