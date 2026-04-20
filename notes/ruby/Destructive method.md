Created: 2023-10-04 13:25

=> A.K.A. [[Mutating method]].

They are the methods that mutate the caller of the [[Method call]], i.e. they change the values of the [[Object]] assigned to the [[Local variable]] without changing their [[Object ID]]. 

They may impact other [[Local variable]] if their [[Assignment]] has let them referencing the same space in memory, e.g.:
![[Pasted image 20231005124204.png]]

They form the **basis of the definition** of [[Mutable]] [[Object]]s (mutability), in Ruby: "*Any class can establish itself as immutable by simply not providing any methods that alter its state.*"

A *user made* [[Method definition]], or a [[Block]], can potentially mutate the **arguments** of a [[Method invocation]], but only by having a built-in destructive method within its body. "*Most methods you will encounter don’t mutate their arguments or caller. Some do mutate their caller, but few mutate the arguments.*" 

[[List of destructive methods]] has a list of [[Method]]s that are capable of mutating the caller.
## References
1. [Intro to Programming with Ruby: Arrays/Modifying Arrays](https://launchschool.com/books/ruby/read/arrays#modifyingarrays)
2. [Intro to Programming with Ruby: More Stuff/Variables as Pointers](https://launchschool.com/books/ruby/read/more_stuff#variables_as_pointers)
3. [Variable References and Mutability of Ruby Objects (articles Part 1)](https://launchschool.medium.com/variable-references-and-mutability-of-ruby-objects-4046bd5b6717)
4. [Mutating and Non-Mutating Methods in Ruby (articles Part 2)](https://launchschool.medium.com/ruby-objects-mutating-and-non-mutating-methods-78023d849a5f)
5. [RB109 Discussion Forum > mutating caller vs argument](https://launchschool.com/posts/adf3e2da)