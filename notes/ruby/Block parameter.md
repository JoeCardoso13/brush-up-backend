Created: 2023-11-05 11:55

**Block** **parameter** is the corresponding [[Variable]] (always [[Local variable]]) in the syntax illustrated below:
```
object_caller.method do |block_parameter|
  # code
end
```
Ruby will treat a *block parameter* much like the left hand side (target variable) of an [[Assignment]] [[Expression]], i.e. it **won't evaluate it**. Using more technical/precise vocabulary, each element will be assigned to the block parameter through [[Object passing]].

When dealing with [[Iteration]]s over [[Hash]]es, the block parameter that takes the element from the [[Collection]] caller can be:
* An [[Array]] with the key-value pair corresponding to positions indexed at 0 and 1.
* A parenthesis with 2 local variables, like: `key, value`. 
The 1st option is only available for some [[Method]]s, while the 2nd is always available.
## References
1. [live session > Beginning Ruby Part 3](https://launchschool.medium.com/live-session-beginning-ruby-part-3-61180782f721)