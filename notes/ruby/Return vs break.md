Created: 2023-10-24 10:32

`Break` is for **iterations** - whereas happening in [[Block]]s or [[Control Expression]] - what `return` is for [[Method invocation]]. 

---

The following example was meant to determine if an input [[String]] has the format of an IP address:
```ruby
def dot_separated_ip_address?(input_string)
  dot_separated_words = input_string.split(".")
  while dot_separated_words.size > 0 do
    word = dot_separated_words.pop
    break unless is_an_ip_number?(word)
  end
  return true
end
```
It contains, however, 2 errors. Doesn't account for more or less than 4 numbers as being invalid IP address, and always returns `true`. Here's the corrected version:
```ruby
def dot_separated_ip_address?(input_string)
  dot_separated_words = input_string.split(".")
  return false unless dot_separated_words.size == 4

  while dot_separated_words.size > 0 do
    word = dot_separated_words.pop
    return false unless is_an_ip_number?(word)
  end

  true
end
```
Note how substituting `break` for `return` changed the logic of the code. 
## References
1. [courses > RB101 > Lesson 3 > Hard 1 set > Question 4](https://launchschool.com/lessons/375f14dd/assignments/567a9e72)