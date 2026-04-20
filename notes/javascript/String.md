Created: 2024-08-19 10:31

Their [[Literal form]] can have either single or double quotes ([[Style guide]] recommends single quotes).

To **interpolate** use backsticks and `${Expression}`:
```javascript
> `5 plus 5 equals ${5 + 5}`
= '5 plus 5 equals 10'
```

The **backslash** character escapes the next character into its form without its syntactical meaning:
```
'He said, \'Hi there!\''  // with single quotes and escaping
"He said, \"Hi there!\""  // with double quotes and escaping
```

JavaScript uses [[Implicit type coercion]] for operations between [[Number]]s and [[String]]s.
## References
1. [ Intro to JS > Basics ](https://launchschool.com/books/javascript/read/basics#datatypes)