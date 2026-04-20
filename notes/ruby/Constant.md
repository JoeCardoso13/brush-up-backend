Created: 2023-10-05 19:34

Technically they only need the first letter to be capitalized. Conventionally all letters are uppercased. They are not supposed to undergo [[Re-assignment]], but Ruby won't throw an [[Exception]] if they do, will simply give a warning.

The [[Constant scope]] is very complex and nuanced. For details see: [[Constant scope]].

Unlike [[Instance variable]]s or [[Class variable]]s, lexically scoped [[Constant]]s can always be reached through the use of the [[Namespacing]] resolution operator: `::` like so:
```ruby
class Computer 
  GREETINGS = ["Beep", "Boop"] 
end

class Person
  def self.greetings
    Computer::GREETINGS.join(', ')
  end

  def greet
    Computer::GREETINGS.sample
  end
end
```

Constants are suitable to avoid prolix [[Method]]s parameters. Once written they'll be accessible within [[Method definition]]s such as in [ RB101 - 119 Small Problems > Easy_4 > convert string to number ](https://launchschool.com/exercises/192719a5)
## References
1. [courses > RB101 > lesson 2 > 18. Variable Scope](https://launchschool.com/lessons/8a39abff/assignments/e3cd8bb9)
2. [ RB101 - 119 Small Problems > Easy_4 > convert string to number ](https://launchschool.com/exercises/192719a5)
3. [ courses > RB120 > lesson 3 > 3. Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b4f9e5b7)
4. [ courses > RB120 > lesson 3 > 4. Inheritance and Variable Scope ](https://launchschool.com/lessons/d2f05460/assignments/b8928e96)