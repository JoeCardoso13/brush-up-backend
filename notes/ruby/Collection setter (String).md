Created: 2023-10-12 14:38

## `String#[]=`

Without [[Ruby's syntactical sugar]]:
```ruby
str = 'abc'
str.[]=(1, 'd')
str # => "adc"
```

* This is actually one of the [[Destructive method]]!!! It mutates the caller:
```
3.2.2 :014 > string = "hey"
 => "hey"
3.2.2 :015 > string.object_id
 => 149860
3.2.2 :016 > string[0]= "wh"
 => "wh"
3.2.2 :017 > string.object_id
 => 149860
```
* However, this method **does not** return a reference to itself!!! It returns a new string:
```ruby
string = "hey"
(string[0]= "wh").<< "foo"
p string # => "whey"
```
* Be aware that when using 2 arguments, the syntax is `String#[start, length]= new_string`:
```ruby
s = 'foo'
s[2] = 'rtune'     # => "rtune"
s                  # => "fortune"
s[1, 5] = 'init'   # => "init"
s                  # => "finite"
```

## References
1. [Ruby Docs 3.2: String](https://docs.ruby-lang.org/en/3.2/String.html#method-i-5B-5D-3D)