Created: 2024-11-18 18:07

Most programming languages divide memory into **two** principal regions: the **stack** and the **heap**. The **stack** doesn't participate in **garbage collection**. JavaScript stores most [[Primitive]] [[Value]]s as well as references on the **stack**, and everything else on the **heap**. You can think of references as pointers to the actual [[Value]] of an [[Object]], [[Array]], or [[String]] that lives in the **heap**.

JavaScript calculates the amount of memory it needs for the **stack** during the creation phase without knowing the specific [[Value]]s. That means it can determine how much **stack** space it needs when **hoisting** occurs. **Stack** [[Value]]s typically must have a fixed size (say, 64 bits). [[Value]]s that don't fit in that size must be stored elsewhere, typically the **heap**. [[String]]s and **BigInts**, for instance, usually can't be stored in 64 bits, so they get placed in the **heap** or somewhere else. However, exactly where these values get stored is an **implementation detail**. As far as you, as a programmer, are concerned, they act like they are on the **stack**, so that's where they are. Since they act like they are on the **stack**, they probably don't participate in **garbage collection**, but, again, that is an **implementation detail**. 

When there are no [[Variable]]s, [[Object]]s, or [[Closure]]s that maintain a reference to the [[Object]] or [[Value]], JavaScript marks the memory as eligible for **GC**. More importantly, as long as the [[Object]] or [[Value]] remains accessible, JavaScript can't, and won't, **garbage collect** it:
```js
function logName() {
  let name = {
    firstName: 'Sarah'          // Declare a variable and set its value. The JavaScript
  };                            // runtime automatically allocates the memory.

  console.log(name.firstName);  // Do something with name
  return name;                  // Returns the `name` object to caller
}

let loggedName = logName();     // loggedName variable is assigned the value stored in name
// which is a reference to the object literal { firstName: "Sarah" }
// The value returned is NOT eligible for GC.
// This value is the same value that is assigned to name
// more code below this line
```

The **heap** rely on **garbage collection** to detect when a [[Value]]'s **reference count** reaches 0. All the garbage collector must do is look for and deallocate [[Value]]s that are eligible for **garbage collection**. If it uses a **reference counting** system, it needs to look for [[Value]]s with a **reference count** of 0. **Garbage collection** can occur at any time; it often occurs at periodic intervals during a program's lifetime. In particular, the programmer usually has no control over when **GC** occurs.

**Garbage collection** is not immune to shortcomings. Here's a simplified example that illustrates it (No modern JavaScript engine uses reference-counting for **garbage collection** anymore):
```js
function go() {
  let foo = {};
  let bar = { qux: foo };
  foo.xyz = bar;
}

go(); // Neither `foo` nor `bar` is eligible for GC
```
In this code, we create two [[Object]]s in `go` that we assign to the `foo` and `bar` local variables. Furthermore, `bar` holds a reference to `foo` in its `qux` property, while `foo` holds a reference to `bar` in its `xyz` property. Both [[Object]]s have reference counts of 2: one reference is to the [[Variable]] to which each [[Object]] is assigned, and the other reference is in a property of the other [[Object]]. When we exit the `go` [[Function]], the reference counts of both [[Object]] get decremented by 1 since both `foo` and `bar` have gone out of scope, so they no longer hold references to the [[Object]]s. However, the two [[Object]]s still exist and are not eligible for **garbage collection** since they still reference each other.

It's important to understand that although [[Closure]] is a concept tightly related to **garbage collection**, [[Variable scope]] is **not**. Here's an example where an out-of-scope [[Variable]] is kept safe from **garbage collection** through [[Closure]]:
```js
function makeFoo() {
  let message = { text: "I'm referenced by an out of scope let!" };

  return function() {
    console.log(message.text);
  };
}

let sayFoo = makeFoo();
sayFoo(); // => I'm referenced by an out of scope let!
```
## References
1. [ JS225 > Closures and function scope > GC ](https://launchschool.com/lessons/0b371359/assignments/48d2a179)