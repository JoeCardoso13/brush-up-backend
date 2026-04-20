Created: 2023-09-30 10:58
# `<=>`

This operator is the basis on which [[Sorting method]]s are construed because it is how [[Comparable module]] evaluates comparisons (except for [[Hash]]es). They are defined independently for each [[Class]].

The `<=>` **compares** two values of the same type and returns -1 , 0 or 1, depending on whether the first [[Object]] is less than, equal to, or greater than the second [[Object]]. If the two [[Object]]s cannot be compared then `nil` is returned.

This is how the following classes employ the [[Spaceship operator]]:
* [[String comparison]]
* [[Symbol comparison]]
* [[Array comparison]]
* [[Integer comparison]]
* [[Float comparison]]
* [[Hash comparison]] (does not)

---

The following [[Method]]s (all defined in the [[Enumerable module]], some in [[Array]] class as well) are also based upon this operator:
- [[min]]
- [[max]]
- [[minmax]]
- [[min_by]]
- [[max_by]]
- [[minmax_by]]
## References
1. [Ruby Docs 3.2: Comparable](https://docs.ruby-lang.org/en/3.2/Comparable.html)
2. [Intro to Programming with Ruby: Flow Control/Comparisons](https://launchschool.com/books/ruby/read/flow_control#comparisons)
3. [the SPOT wiki > Assignment_preparation.pdf](https://fine-ocean-68c.notion.site/SPOT-Wiki-b58ff38ab84440bdb96797e59ee5fd34)
4. [courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)