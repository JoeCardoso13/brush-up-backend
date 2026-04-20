Created: 2024-08-19 12:24

There are many style guides for JavaScript and most teams have their own. A good one is the one from AirBnb: https://github.com/airbnb/javascript

Some general best practices to avoid problems with [[Hoisting]], [[Variable scope]] etc:
* Prefer `let` and `const` over `var`.
* If you must use `var` have the [[Variable declaration]] on top of the [[Variable scope]].
* Have `let` and `const` [[Variable declaration]]s close to their usage.
* Use [[Function declaration]]s before [[Function call]]s.
* Use trailing commas for multi-line simple [[Object]] definition.
* Use dot notation instead of brackets to access [[Object]] properties when possible.
## References
1. [ AirBnB style guide ](https://github.com/airbnb/javascript)