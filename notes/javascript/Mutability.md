Created: 2024-08-19 14:39

Some [[Function]]s and [[Method]]s mutate the argument or caller. Others don't. The same can be said about [[Variable (re)assignment]]s.

A very frequent (thereby **important**) case is the reassigning of an [[Object]] property:
```js
> let a = { a: 1, b: 2, c: 3 };
undefined
> let b = a;
undefined
> b['b'] = 13;
13
> a
{ a: 1, b: 13, c: 3 }
```
[[Copying an object]] is a way to counter this behavior. However, in most cases, it doesn't work for **nested structures** (be them [[Array]] or simple [[Object]]s).

Here are some [[Method]]s that are destructive:
* [[Sort]]
* [[Reverse]]
* [[Push]]
* [[Pop]]
* [[Shift]]
* [[Unshift]]
* [[Splice]]
## References
1. [ Intro to JS > Reassignment and Mutation ](https://launchschool.com/books/javascript/read/functions#reassignmentandmutation)