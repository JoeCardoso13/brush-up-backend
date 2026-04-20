Created: 2024-01-05 08:58

Ruby defines the [[State]]s and [[Behavior]]s of its [[Object]]s in **classes**. You can think of classes as basic outlines of what an [[Object]] should be made of - its [[State]] - and what it should be able to do - its [[Behavior]].

The classes themselves may have their own [[Class method]]s and [[Class variable]]s.

---
* Use the CamelCase naming convention to create the class name.
* `Object#class` [[Return value]] is the [[Class]] of the object responsible for the [[Method call]]:
 ```
> "hello".class
=> String
> "world".class
=> String
```

## References
1. [ LS books / Ruby OOP / the object model ](https://launchschool.com/books/oo_ruby/read/the_object_model)
2. [ LS books / Ruby OOP / classes and objects II ](https://launchschool.com/books/oo_ruby/read/the_object_model)