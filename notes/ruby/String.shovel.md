Created: 2023-10-23 10:10

Concatenates `object` to `self` and returns `self`:
```ruby
s = 'foo'
s << 'bar' # => "foobar"
s          # => "foobar"
```
*If `object` is an Integer, the value is considered a codepoint and converted to a character before concatenation.*

Related: [[String.concat]], which takes **multiple arguments**.
## References
1. [Ruby Docs 3.2: string/Shovel](https://docs.ruby-lang.org/en/3.2/String.html#method-i-3C-3C)