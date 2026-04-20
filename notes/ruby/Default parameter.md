Created: 2023-10-02 10:12

Parameters can be set as **optional** in a [[Method definition]] using the following syntax:
```ruby
def say(words='hello')
  puts words + '.'
end

say()      # <= prints hello.
say("hi")  # <= prints hi.
```

---

[[Hash]] can add even more flexibility:
```ruby
def greeting(name, options = {})
  if options.empty?
    puts "Hi, my name is #{name}"
  else
    puts "Hi, my name is #{name} and I'm #{options[:age]}" +
         " years old and I live in #{options[:city]}."
  end
end

greeting("Bob")
greeting("Bob", {age: 62, city: "New York City"})
```

Be aware, though, that if the default parameter [[Variable]] is not used, it does not incur in [[Initialization]]:
```
> class Student
>   attr_accessor :grade
>   def initialize(name, grade=nil)
>     @name = name
>   end
> end
> ade = Student.new('Adewale')
 => #<Student:0x00007f7dc17eb2d8 @name="Adewale">
```
## References
1. [Intro to Programming with Ruby: Methods](https://launchschool.com/books/ruby/read/methods) 
2. [Ruby Docs 3.2: syntax/methods/Default Values](https://docs.ruby-lang.org/en/3.2/syntax/methods_rdoc.html#label-Default+Values)