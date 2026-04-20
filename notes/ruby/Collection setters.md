Created: 2023-10-07 10:20

Are all examples of [[Mutating method]]s. They have the form `#[]=` and mutate the original [[Object]]. They are not actually [[Assignment]]s. They only appear to be so due to Ruby's [[Ruby's syntactical sugar]]. 

Examples:
* [[Collection setter (Array)]]
* [[Collection setter (String)]]
* [[Collection setter (Hash)]]

Be aware that *these collection setters* may also come in the short-hard abbreviation form: `+=`, `-=`, `*=` etc. 

Moving into [[OOP]] you can make your own custom collection setters like so:
```ruby
class MyCollection
# ...
  def []=(idx, obj)
    # Body of custom made collection setter
  end
# ...
end
```
## References
1. [Variables References and Mutability of Ruby Objects (articles: Part 1)](https://launchschool.medium.com/variable-references-and-mutability-of-ruby-objects-4046bd5b6717)