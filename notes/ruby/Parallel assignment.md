Created: 2023-12-18 11:50

Because of the order which [[Assignment]] [[Expression]]s are evaluated, you can avoid using temporary storage [[Local variable]]s this way:
```ruby
def swap_first_last_characters(word)
  word[0], word[-1] = word[-1], word[0] 
  word
end
```

Moreover, it makes it a lot easier to swap [[Array]] elements when used within a [[Block]] argument of [[map Method]] being called by said [[Array]] with index.
## References
1. [ RB101-RB119 Small Problems > Easy 5 > letter swap ](https://launchschool.com/exercises/56e92849)
2. [ RB101-RB119 Small Problems > Easy 6 > reversed arrays P1 ](https://launchschool.com/exercises/eec5e591)