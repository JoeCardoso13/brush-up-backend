Created: 2023-10-21 13:40

Its [[Return value]] is the name of the [[Local variable]]s of the current [[Variable Scope]] in [[Array]] format.

```ruby
fred = 1
for i in 1..10
   # ...
end
local_variables   #=> [:fred, :i]
```
## References
1. [Ruby Docs 3.2: kernel/local_variables](https://docs.ruby-lang.org/en/3.2/Kernel.html#method-i-local_variables)