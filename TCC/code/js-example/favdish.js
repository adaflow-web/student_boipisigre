/*

    Create a JavaScript array to store your 3 favorite dish.
    List each of them in the console on their own separate line.
    Display the count of your favorite dishes.
    Add a 4th dish to the array.
    Display the count once more within a sentence such as "I have x favorite dishes."
    Remove the 2nd one!
    Sort them in alphabetical order.
    Display them once more but this time as an array in the console.
    Display the count again!
*/
// 1
var favdish = ["Salade", "Gratin Dauphinois", "Raclette"];

// 2
console.log(favdish[0]);
console.log(favdish[1]);
console.log(favdish[2]);

// 3
console.log(favdish.length) ;

favdish.push("Poulet");
console.log("ajout de poulet")
console.log("I have " + favdish.length + " favorite dishes.");

favdish.splice(1,1);

favdish.sort();
console.log(favdish);

console.log(favdish.length) ;
