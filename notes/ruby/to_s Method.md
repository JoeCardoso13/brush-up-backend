Created: 2024-01-19 13:11

If not **overridden** by another `#to_s` further down the [[Method lookup path]], the default [[Return value]] of this [[Method]] is determined by how it's defined in the [[Object]] [[Class]]. I.e. :
"The default [`to_s`](https://docs.ruby-lang.org/en/3.2/Object.html#method-i-to_s) prints the [[Object]]’s [[Class]] and an encoding of the [[Object ID]]."

When overriding (customizing) `#to_s` for use in a custom [[Class]], you **must remember** that Ruby expects `#to_s` [[Return value]] to **always** be a [[String]]. If not, Ruby will **ignore** the non-[[String]] value and look in the [[Inheritance]] chain for another version of `#to_s` that does return a [[String]]. It will probably be the default mentioned above.

It is automatically used by Ruby when:
1) [[String]] [[Interpolation]]
2) `Kernel#puts` [[Method]]
## References
1. [ Ruby Docs 3.2: Object/to_s ](https://docs.ruby-lang.org/en/3.2/Object.html#method-i-to_s)
2. [ OOP with Ruby > Classes and Objects II > The to_s Method](https://launchschool.com/books/oo_ruby/read/classes_and_objects_part2#theto_smethod)
3. [ courses > RB120 > lesson 4 > Practice Problems Easy 1 > Question 6 ](https://launchschool.com/lessons/f1c58be0/assignments/a5cfd2ae)
4. [ courses > RB120 > lesson 1 > discussions > 'understanding return'... ](https://launchschool.com/posts/e1f64bb6)