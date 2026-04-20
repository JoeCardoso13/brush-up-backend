Created: 2024-11-19 09:27

Immediately Invoked [[Function expression]]

They are particularly useful to seal-off code from the rest of the code, for instance:
```js
// thousands of lines of messy JavaScript code!

(function(type, name) {
  var myPet = {
    type,
    name,
  };

  console.log(`I have pet ${myPet.type} named ${myPet.name}`);
})('Dog', 'Spot');

// more messy JavaScript code
```
Doing it can help debugging. 

It is also useful for controlling access to [[Private data]]. Let's say we want to have an `inventory` [[Object]] with [[Method]]s to act on a `stocks` data, but we need it to be [[Private data]]:
```js
let inventory = (function() {
  let stocks = [];
  function isValid(newStock) {
    return stocks.every(function(stock) {
      return newStock.name !== stock.name;
    });
  }

  return {
    stockCounts() {
      stocks.forEach(function(stock) {
        console.log(stock.name + ': ' + String(stock.count));
      });
    },
    addStock(newStock) {
      if (isValid(newStock)) { stocks.push(newStock) }
    },
  };
})();
```
This fine-tuning of public-interface control is a core feature of [[Encapsulation]].
## References
1. [ JS 225 > Closures and function scope ](https://launchschool.com/lessons/0b371359/assignments/470d67c3)