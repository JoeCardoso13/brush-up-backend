Created: 2023-10-08 11:01

Every computer programming language uses some sort of _evaluation strategy_ when passing objects. The most common strategies are known as _strict evaluation_ strategies. With strict evaluation, every [[Expression]] is evaluated and converted to an [[Object]] before it is passed along to [[Method]]. Ruby uses strict evaluation exclusively. The two most common strict evaluation strategies are pass by value and pass by reference.

Ruby employs a mixture of both. Ruby passes a copy of the [[Object]] reference to the [[Method]]. Ruby acts like a pass by reference for the most part, by:
* Being able to mutate the argument.
* Keeping the same [[Object ID]] when a variable is passed, i.e showing [[Variables as pointers]] behavior.
However, Ruby cannot do **one thing** that a purely pass by reference would be able to, which is:
* [[Re-assignment]] of the argument of a [[Method call]].

In a purely pass by reference language, [[Assignment]] is a mutating operation. Ruby appears to be making copies of the references, then passing those copies to the method. *The method can use the references to mutate the referenced [[Object]], but since the reference itself is a copy, the original reference given by the argument cannot be reassigned.*
## References
1. [Object Passing in Ruby - Pass by Reference or Pass by Value (articles Part 3)](https://launchschool.medium.com/object-passing-in-ruby-pass-by-reference-or-pass-by-value-6886e8cdc34a)