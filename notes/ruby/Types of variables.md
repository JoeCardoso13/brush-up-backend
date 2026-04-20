Created: 2023-09-29 10:47

1. Constants are declared by capitalizing every letter in the variable's name, per Ruby convention: 
```ruby
MY_CONSTANT = 'I am available throughout your app.'
```
2. Global variables are declared by starting the variable name with the dollar sign (`$`). 
```ruby
$var = 'I am also available throughout your app.'
```
3. Class variables are declared by starting the variable name with two `@` signs. These variables are accessible by instances of your class, as well as the class itself. 
```ruby
@@instances = 0
```
4. Instance variables are declared by starting the variable name with one `@` sign.  These variables are available throughout the current instance of the parent class. 
```ruby
@var = 'I am available throughout the current instance of this class.'
```
5. [[Local variable]] are the most common variables you will come across and obey all scope boundaries. 
```ruby
var = 'I must be passed around to cross scope boundaries.'
```
## References
1. [Intro to Programming with Ruby: The Basics/Variables/Types of Variables](https://launchschool.com/books/ruby/read/variables#typesofvariables)