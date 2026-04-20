Created: 2023-11-09 16:16

|Method|Action|Considers the return value of the block?|Returns a new collection from the method?|Length of the returned collection|
|---|---|---|---|---|
|`each`|Iteration|No|No, it returns the original|Length of original|
|`select`|Selection|Yes, its truthiness|Yes|Length of original or less|
|`map`|Transformation|Yes|Yes|Length of original|

This is how their [[Return value]] compare ([[map Method]] returns an [[Array]]) against each other:
```
> {}.each {}
 => {}
> {}.select {}
 => {}
> {}.map {}
 => []
```
## References
1. [courses > RB110 > Lesson 1 > The Each, Map and Select Methods](https://launchschool.com/lessons/6a5eccc0/assignments/da1f87fe)