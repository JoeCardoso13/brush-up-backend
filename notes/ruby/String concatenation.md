Created: 2023-10-23 09:53

## `String#+`

Non-mutating method, commonly used in [[Assignment]] expressions as follows:
```
a = 'The result is ' + result.to_s
```
It is to be **avoided** as per [Ruby Style Guide](https://rubystyle.guide/#strings).

**Different** from [[String.concat]] or [[String.shovel]] in that it returns a new string, it is **not** like the latter [[Destructive method]]. 
## References
1. [courses > RB101 > lesson 3 > Hard 1 > Question 2](https://launchschool.com/lessons/375f14dd/assignments/567a9e72)
2. [Ruby Docs 3.2: strings/Concatenation](https://docs.ruby-lang.org/en/3.2/String.html#method-i-2B)