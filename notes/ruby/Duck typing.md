Created: 2024-02-14 15:42

**Duck typing** occurs when [[Object]]s of different _unrelated_ types both respond to the same [[Method]] name. With duck typing, we aren't concerned with the [[Class]] or type of an [[Object]], but we do care whether an [[Object]] has a particular [[Behavior]]. _If an object quacks like a duck, then we can treat it as a duck._ Specifically, **duck** **typing** is a form of [[Polymorphism]]. As long as the [[Object]]s involved use the same [[Method]] name and take the same number of arguments, we can treat the [[Object]] as belonging to a specific category of [[Object]]s.

For example, an application may have a variety of elements that can respond to a mouse click by calling a [[Method]] named something like `handleClick`. Those elements may be completely different -- for instance, a checkbox vs. a text input field -- but they're all _clickable_ [[Object]]s. Duck typing is an informal way to classify or ascribe a type to [[Object]]s. [[Class]]es provide a more formal way to do that.

Here is an example of code designed with **duck typing**:
```ruby
class Wedding
  attr_reader :guests, :flowers, :songs

  def prepare(preparers)
    preparers.each do |preparer|
      preparer.prepare_wedding(self)
    end
  end
end

class Chef
  def prepare_wedding(wedding)
    prepare_food(wedding.guests)
  end

  def prepare_food(guests)
    #implementation
  end
end

class Decorator
  def prepare_wedding(wedding)
    decorate_place(wedding.flowers)
  end

  def decorate_place(flowers)
    # implementation
  end
end

class Musician
  def prepare_wedding(wedding)
    prepare_performance(wedding.songs)
  end

  def prepare_performance(songs)
    #implementation
  end
end
```

Note that merely having two different [[Object]]s that have a [[Method]] with the same name and compatible arguments doesn't mean that you have [[Polymorphism]]. In theory, those [[Method]]s might be used polymorphically, but that doesn't always make sense. Consider the following two [[Class]]es:
```ruby
class Circle
  def draw; end
end

class Blinds
  def draw; end
end
```
Forcibly, you could use these [[Method]]s 'polymorphically'. However, it's unlikely that this would ever make sense in real code. Unless you're actually calling the [[Method]] in a polymorphic manner, you don't have [[Polymorphism]].
## References
1. [ courses > RB120 > lesson 2 > Polymorphism and Encapsulation ](https://launchschool.com/lessons/dfff5f6b/assignments/8c6b8604)