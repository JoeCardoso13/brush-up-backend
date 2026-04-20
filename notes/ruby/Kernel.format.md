Created: 2023-11-15 09:29

=> A.K.A. *sprintf*

It formats [[Object]]s when doing [[String]] [[Interpolation]]. 

A format **specification** has the form:
```
%[flags][width][.precision]type
```

Example:
```
> format('Now is %.2d:%.2dAM', 5, 5)
 => "Now is 05:05AM"
```

When the **specification** has the form:
```
%{variable}
```
Then format takes a [[Hash]] as the second argument. They keys of the [[Hash]] will be used to match the `variable` and the output will be the correspondent value.
## References
1. [Ruby Docs 3.2: format specifications](https://docs.ruby-lang.org/en/3.2/format_specifications_rdoc.html)
2. [ Ruby Docs 3.2: format specifications / reference by name](https://docs.ruby-lang.org/en/3.2/format_specifications_rdoc.html#label-Reference+by+Name)
3. [ RB101-RB119 Small Problems > Advanced_1 > madlibs revisited ](https://launchschool.com/exercises/3dd7dd43)