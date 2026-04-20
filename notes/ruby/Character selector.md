Created: 2023-10-16 11:49

They are written as [[String]] [[Literal]]s and can be used as arguments for a few [[String]] [[Method]]s listed below. 

A character selector identifies zero or more characters in the [[Object]] caller that are to be operands for the method. In a character selector, these three characters get special treatment: 
* A leading caret (`'^'`) functions as a “not” operator for the characters to its right:
```ruby
'abracadabra'.delete('^bc') # => "bcb"
'0123456789'.delete('^852') # => "258"
```
* A hyphen (`'-'`) between two other characters defines a range of characters instead of a plain string of characters:
```ruby
'abracadabra'.delete('a-d') # => "rr"
'0123456789'.delete('4-7')  # => "012389"
```
* A backslash (`'\'`) acts as an escape for a caret, a hyphen, or another backslash.

Each of these [[Method]]s accepts one or more character selectors:

- [[String.tr]] : optional `!`, takes only 1 character selector.
- [[String.tr_s]]: optional `!`, takes only 1 character selector.
- [[String.count]]
- [[String.delete]]: optional `!`. 
- [[String.squeeze]]: optional `!`.
## References
1. [Ruby Docs 3.2: character selectors](https://docs.ruby-lang.org/en/3.2/character_selectors_rdoc.html#label-Character+Selectors)
2. [RB101-RB109 - Small Problems > Easy 3 > Palindromic Strings (Part 2)](https://launchschool.com/exercises/8fca300b)