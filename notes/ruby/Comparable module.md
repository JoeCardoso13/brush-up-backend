Created: 2023-11-03 10:22

The module [`Comparable`](https://docs.ruby-lang.org/en/3.2/Comparable.html) uses the [[Spaceship operator]] defined for each [[Class]] to implement the conventional comparison operators (the [[Method]]s `<`, `<=`, `==`, `>=`, and `>`). 

This is how the following classes employ the [[Spaceship operator]]:
* [[String comparison]]
* [[Symbol comparison]]
* [[Array comparison]]
* [[Integer comparison]]
* [[Float comparison]]
* [[Hash comparison]]

---

When building custom [[Method]]s for [[Class]]es, by including the comparable module and defining a [[Spaceship operator]] [[Instance method]], the instance [[Object]]s of that [[Class]] will have access to comparison operators (the [[Method]]s `<`, `<=`, `==`, `>=`, and `>`).
## References
1. [Intro to Programing with Ruby > Flow Control > Summary](https://launchschool.com/books/ruby/read/flow_control#summary)
2. [courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)
3. [ Ruby Docs 3.2: comparable ](https://docs.ruby-lang.org/en/3.2/Comparable.html)