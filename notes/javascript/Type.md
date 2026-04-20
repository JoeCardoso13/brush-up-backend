Created: 2024-08-19 10:07

Type in JavaScript is what more traditional OO languages call [[Class]]. In [[Object Oriented]] programming, we often refer to individual [[Object]]s of a specific data type as **instances** of that type. An **instance** is just another **term** for the [[Object]]s created using any means of defining multiple [[Object]]s of the same kind (like the patterns to [[Create object]]s). In the case of [[Object factory]] pattern, the type of the **instances** can't be found/tested in code. 

JavaScript has 2 categories of data types:
* [[Primitive]]
* [[Object]]
It is important to understand their behavior in terms of [[Mutability]]. The former type is **immutable** while the latter is **mutable**. Also, you can't meaningfully use [[Strict equality]] directly on the latter, while it works fine on the former.

We should always aim to use [[Explicit type coercion]] but sometimes it is necessary to know about how JS handles [[Implicit type coercion]]. 

## References
1. [ Intro to JS > Basics ](https://launchschool.com/books/javascript/read/basics#datatypes)