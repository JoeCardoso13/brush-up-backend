Created: 2024-11-14 10:36

In JS the number of parameters in the [[Function definition]] and the number of arguments provided in the [[Function call]] (or [[Method call]]) don't have, in their interplay, any constraint that could cause an error to be raised. Non assigned parameters are given [[Undefined]] [[Value]]s and extra arguments (more than prescribed in the [[Function definition]]) are simply ignored.

## References
1. [ Intro to JS > Functions ](https://launchschool.com/books/javascript/read/functions#threewaystodefineafunction)