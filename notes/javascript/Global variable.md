Created: 2024-08-19 12:38

[[Variable]]s that have their [[Variable declaration]] in the global [[Variable scope]] are global [[Variable]]s. They are available (to read and write) throughout the program:
```js
let greetingMessage = "Good Morning!"; // global variable

function greetPeople() {
  console.log(greetingMessage);
}

function changeGreetingMessage(newMessage) {
  greetingMessage = newMessage;
}

changeGreetingMessage("Good Evening");
greetPeople(); // => 'Good Evening'
```

Their use should be limited. To avoid bugs [[Variable]]s should be given the smallest [[Variable scope]] possible.
## References
1. [ Intro to JS > Functions & Scope ](https://launchschool.com/books/javascript/read/functions#functionsscope)