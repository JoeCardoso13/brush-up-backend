Created: 2023-11-09 14:54

Some [[Control Expression]] can perform iterations, such as [[for Loop]], [[while Loop]] and [[until Loop]]. The [[Kernel.loop()]] method is also pretty generic for building iterations.

Most often it is more convenient to use built-in [[Method]]s when performing iterations. The following [[Method]]s, defined by classes considered [[Collection]]s, are capable of iterating: 

* [[each Method]]
* [[Enumerable.each_with_index]] & [[Enumerator.with_index]]
* [[Numeric.step]]
* [[Integer.times]]
* [[String.each_char]]
* [[String.each_codepoint]]
* [[Integer.upto(Integer)]]
* [[Array.zip]]
* [[Array.product]]
* [[Array.permutation]]
* [[Array.combination]]

**Never** use [[Destructive method]]s on the [[Object]] caller of the iteration!
## References
1. [courses > RB110 > lesson 1 > 7. Selection and Transformation](https://launchschool.com/lessons/6a5eccc0/assignments/d8fd867a)
2. [courses > RB110 > lesson 2 > 4. Working with Blocks](https://launchschool.com/lessons/fa1f5e7e/assignments/084fe222)