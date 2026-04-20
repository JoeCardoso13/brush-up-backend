Created: 2023-10-05 13:02

## Basics
When returned, if not accompanied by an [[Exception handling]] process, will stop the program from continue running (crash). Will contain the *stack trace* which shows the [[Call stack]] at the moment the **error** was **raised**.

---
## Intermediate
They are organized into [[Class]]es (see Ruby's [[Exception class hierarchy]]), at the very top is the **Exception** [[Class]] itself. Most often, the **errors** you want to **handle** are descendants of the `StandardError` [[Class]].

Exception [[Object]]s are just normal Ruby [[Object]]s that we can gain useful information from. Some useful [[Instance method]]s that Ruby provides are `Exception#message` and `Exception#backtrace`, which return an **error** **message** and a **backtrace** associated with the **exception**, respectively.

[[Exception raising]] allows us to manually **raise** **exceptions**.
## References
1. [Intro to Programming with Ruby: More Stuff: Exception Handling](https://launchschool.com/books/ruby/read/more_stuff#exceptionhandling)
2. [ Getting Started With Ruby Exceptions (article)](https://launchschool.medium.com/getting-started-with-ruby-exceptions-d6318975b8d1)
3. [ Ruby Docs 3.2: Exception ](https://docs.ruby-lang.org/en/3.2/Exception.html)