var fruits = ["oranges", "apples", "bananas"];
console.log(fruits);

var message = "The second value contains apples: " + fruits[1];
console.log(message);

fruits[1] = "kiwis";
var message = "The second value now contains kiwis: " + fruits[1];
console.log(message);
console.log(fruits);

fruits.push("tomatoes");
console.log(fruits);

fruits.splice(2, 3);
console.log(fruits);

fruits.push("tomatoes");
fruits.push("peachs");
console.log(fruits);

fruits.splice(2, 2);
console.log(fruits);
