Created: 2023-10-23 10:05

Concatenates each object in `objects` to `self` and returns `self`:
```ruby
s = 'foo'
s.concat('bar', 'baz') # => "foobarbaz"
s                      # => "foobarbaz"
```
*For each given object `object` that is an Integer, the value is considered a codepoint and converted to a character before concatenation.*

Related: [[String.shovel]], which takes a **single argument**.
## References
1. [Ruby Docs 3.2: string/Concat](https://docs.ruby-lang.org/en/3.2/String.html#method-i-concat)