Created: 2023-09-29 12:28

* Can be a new [[Object]] or an existing [[Object]].

* **Commonly referred to as** the value that a [[Method invocation]] will return. "*Just as much as arguments are passed to methods, return values are passed by those methods back to the caller.*" Ruby [[Method]] always return the evaluated result of the last [[Expression]] executed in their [[Method definition]]s unless an explicit `return` keyword comes before it.

* The `return` keyword will exit running [[Method]] even if within [[Control Expression]] iterations (as shown in [[Return vs break]]).

* Return values are foundational for [[Method chain]]. They may also be simultaneously generated and used for [[Method call]]s, when nesting [[Method]].

* It can also be referred to, in slightly looser language, as the value that a [[Block]] returns. 

* Technically, every [[Expression]] (e.g. [[Control Expression]]) returns **a** value (or an [[Exception]]) and pretty much everything you can write in Ruby is an [[Expression]]. But these ordinary values returned by expressions are usually referred to as what the [[Expression]] "*evaluates to*", they are not **the** return value from [[Method call]], although in very loose language the terms used can be interchangeable.
## References
1. [Intro to Programming with Ruby: The Basics/nil](https://launchschool.com/books/ruby/read/basics#nil)
2. [Ruby Docs 3.2: syntax/methods/Return Values](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Return+Values)
3. [Object Passing in Ruby - Pass by Reference or Pass by Value (articles Part 3)](https://launchschool.medium.com/object-passing-in-ruby-pass-by-reference-or-pass-by-value-6886e8cdc34a)
4. [the SPOT wiki > Assignment_preparation.pdf](https://fine-ocean-68c.notion.site/SPOT-Wiki-b58ff38ab84440bdb96797e59ee5fd34)