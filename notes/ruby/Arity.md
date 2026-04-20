Created: 2024-03-22 14:56

It's the rule that deals with the relationship between the number of parameters of source and client codes. Specifically:
1) **Strict** **arity**: is the rule for [[Method]]s and Lambdas. E.g. [[Method definition]]s **must** have the same number of parameters as its corresponding [[Method call]] otherwise an [[Exception]] (`ArgumentError`) is raised.
2) **Lenient** **arity**: is the rule for [[Block]]s and [[Proc]]s. E.g. if the [[Yield]] uses more arguments than there are corresponding [[Block parameter]]s, nothing happens, and in case they're less, the unfulfilled [[Block parameter]]s are assigned to `nil` (similar to uninitialized [[Instance variable]]s).

Note that the arity rule for [[Block]]s is in respect to the parameters of [[Yield]] and the [[Block parameter]]s. It is **not** about the use of [[Yield]] without a [[Block]] and [[Block]] without an [[Yield]].

For a more thorough explanation, see reference # 2.
## References
1. [ courses > RB130 > lesson 1: blocks > writing methods that take blocks ](https://launchschool.com/lessons/c0400a9c/assignments/5a060a20)
2. [ Ruby Docs 3.2: syntax / arguments ](https://docs.ruby-lang.org/en/3.2/syntax/calling_methods_rdoc.html#label-Arguments)