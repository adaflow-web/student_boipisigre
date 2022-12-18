console.log("boucle for")

for (var i = 1; i < 4; i = i + 1) {
  console.log("Step: " + i.toString());
  console.log("Pas: " + i); // OK mais pas bien
}
console.log("fini")

console.log("boucle while")

var i=1;
while (i<4) {
  console.log("Pas: " + i.toString());
  i=i+1;
}
