function isGreatherThan10(number) {
  if (number > 10) {
    return "The number is greater than 10.";
  } else {
    return "The number is smaller than 10.";
  }
}

var valeur = 11;
message = isGreatherThan10(valeur);
console.log(message);

var valeur = 5;
message = isGreatherThan10(valeur);
console.log(message);
