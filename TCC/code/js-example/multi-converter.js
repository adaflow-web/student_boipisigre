function convertcel(celciustemp){
    var faren = (( celciustemp*9)/5)+32
    return faren
  }

function convertgalon(galon){
      var litre = galon * 3.785411784
      return litre
    }

function convertdolar(dolar){
  var chf = dolar *  0.9299
        return chf
      }
// var vNan=  NaN ;

var ok =window.prompt("Voulez vous convertir - O/n") ;
while (ok == "O" || ok == "o") {

var conv =window.prompt("convertion Celsius/Dollar/Galon - C/D/G") ;
var value =window.prompt("Quel valeur souhaitez convertir - nombre") ;

// var saisie=Number(value);

// console.log(Number(value)+ " " + vNan ) ;


if ( isNaN(value) != true && value != "" ) {
switch(conv) { // remplace des if multiples.
  case "C":
  case "c":
    console.log(value +  "°C est égale à "+convertcel(value) + "°F");
    break;
  case "G":
  case "g":
    // code block
    console.log(value +  " Galon est égale à "+convertgalon(value) + "litres");
    break;
  case "D":
  case "d":
console.log(value +  " $ est égale à "+convertdolar(value) + "chf");
// code block
      break;
  default:
  console.log("Désolé nous n'avons pas de convertisseur")
    // code block
  }
  }
  else { console.log("votre saisie n'est pas un nombre")}

var ok =window.prompt("Voulez vous continuer à convertir - O/n") ;
}
console.log("bye-bye");
