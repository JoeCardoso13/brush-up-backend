Created: 2023-10-06 10:30

The way Ruby references a place in memory is through object ID's.

The [[Object]] class has the method `#object_id` built-in, that can be used to access an object ID. All classes represented by [[Literal]] have access to this method either by having the [[Object]] class as its parent ([[Array]], [[Hash]], [[String]] and [[Symbol]])  or grand-parent ([[Integer]] and [[Float]]).   
## References
1. [Variables Reference and Mutability of Ruby Objects (article)](https://launchschool.medium.com/variable-references-and-mutability-of-ruby-objects-4046bd5b6717)
2. [Ruby Docs 3.2: object/Object ID](https://docs.ruby-lang.org/en/3.2/Object.html#method-i-object_id)