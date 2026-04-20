Created: 2023-10-15 11:07

The Time class can return current year, month or day. Using class method `::new` an [[Object]] is created that can provide a lot of time-related information. It also has a [[Return value]] of [[String]] type that contains information that will depend on the parameters used.

This class can be quite useful when cross-referencing days, months and years. For instance, here is a small piece of code ([[Method]]) that gives you the number of Friday 13ths on a given year:
```ruby
def friday_13th(year)
  count = 0
  1.upto(12) do |month|
    count += 1 if Time.new(year, month, 13).friday?
  end
  count
end
```
## References
1. [Ruby Docs 3.2: Time](https://docs.ruby-lang.org/en/3.2/Time.html#class-Time)
2. [RB101-RB119 - Small Problems > Easy 2 > When Will I Retire?](https://launchschool.com/exercises/d28a76d4)
3. [ RB101-RB119 - Small problems > Medium 2 > Unlucky Days ](https://launchschool.com/exercises/a7fce257)