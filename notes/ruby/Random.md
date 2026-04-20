Created: 2023-10-15 11:02

The Random class is Ruby's source of randomness. The method `Random.rand` provides functionality for `Kernel.rand`. Negative or [[Float]] arguments should be avoided.
* If called without argument, or `arg#to_i == 0` is true, returns a pseudo-random floating point number between 0.0 and 1.0 .
* If called with number argument greater or equal to 1, returns a pseudo-random integer greater than or equal to 0 and less than `arg#to_i`.
* If called with [[Range]] argument, its [[Return value]] is a random element of [[Range]].
## References
1. [Ruby Docs 3.2: Random](https://docs.ruby-lang.org/en/3.2/Random.html)
2. [RB101 - RB109 - Small Problems > Easy 2 > How old is Teddy?](https://launchschool.com/exercises/84376930)