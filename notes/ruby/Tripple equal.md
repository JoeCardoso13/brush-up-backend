Created: 2023-12-20 10:15

When `#===` compares two objects, it's essentially asking "if `obj1` is a group, would `obj2` belong in that group?"
```ruby
String === "hello" # => true
String === 15      # => false
```
Syntax:
```ruby
Container === contained # => true
```
Be aware that:
```
> Integer === 1
 => true
> Integer == 1
 => false
```

This is what is implicitly used for [[case Expression]]s. 

Similar to `==` it is defined by the [[Class]].
## References
1. [ Ruby Docs 3.2: Enumerable / anyQM ](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-any-3F)
2. [ courses > RB110 > lesson 1 > Discussions > How do these... ](https://launchschool.com/posts/fff43a91)