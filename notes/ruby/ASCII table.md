Created: 2023-10-19 15:21

Some useful rules to remember are:
- Uppercase letters come before lowercase letters
- Digits and (most) punctuation come before letters
- There is an _extended_ ASCII table containing accented and other characters - this comes after the main ASCII table (`'b' <=> '}' # => -1`)

The [[String]] [[Spaceship operator]] is based upon the ASCII table. `String#ord` returns the ASCII position of a character, `Integer#chr` goes the other way around.

All positive [[Integer]]s bears the same position in the ASCII table, i.e. **49** (negatives are **45**).

The [[Method]]s that provide direct conversion are:
* [[Integer.chr]]
* [[String.ord]]
## References
1. [the SPOT wiki > Assignment_preparation.pdf](https://fine-ocean-68c.notion.site/SPOT-Wiki-b58ff38ab84440bdb96797e59ee5fd34)
2. [courses > RB110 > lesson 2 > 2. Sorting](https://launchschool.com/lessons/fa1f5e7e/assignments/a6713515)
3. [Wikipedia](https://en.wikipedia.org/wiki/ASCII#Code_chart)