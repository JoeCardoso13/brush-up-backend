Created: 2023-12-08 08:05

With this [[Method]] you provide the [[Object]] (as a [[Literal]] or a reference) as an argument of the [[Method call]], and can refer to it from within the [[Block]]:
```
3.2.2 :001 > a = []
 => []
3.2.2 :002 > a.object_id
 => 11560
3.2.2 :003 > { foo:1, bar: 2, baz: 3 }.each_with_object(a) { |(k, v), a| a << [k, v] }
 => [[:foo, 1], [:bar, 2], [:baz, 3]]
3.2.2 :005 > a.object_id
 => 11560
```

Its [[Return value]] is the (potentially) transformed [[Object]] given as argument, it differs from [[Enumerable.each_with_index]] in this. For each [[Iteration]], when the [[Return value]] of the [[Block]] is [[Falsy]], it does **not** get added to the [[Object]] given as argument (which is a significant deviation from the [[map Method]] and [[Enumerable.inject()]]):
```
> { a: 1, b: 2 }.each_with_object({}) do |(k, v), obj|
>   nil
> end
 => {}
``` 

Returns an [[Enumerator]] if no [[Block]] is given.
## References
1. [ Ruby 3.2: Enumerable/ each with object](https://docs.ruby-lang.org/en/3.2/Enumerable.html#method-i-each_with_object)
2. [ courses > RB110 > lesson 1 > Quizz > Question 19 ](https://launchschool.com/quizzes/7dc41e74)