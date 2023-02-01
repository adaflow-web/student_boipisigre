
function lirenom() {
//  console.log(localStorage.length) ;
// if (localStorage.length> 0) {
if (localStorage.length >0) {

  var personne =localStorage.getItem("NomUtilisateur" );
  document.getElementById("name").innerHTML = ""  + personne;
   }
else {
  window.location.href = "/clear";
  // let personne = prompt("Bonvolu skribas vian nomon", "Zamenov");
}

}

function save_data() {
    var input = document.getElementById("message");
    localStorage.setItem("NomUtilisateur", input.value);
    //var storedValue = localStorage.getItem("server");
    // etc..
  }



function clearnom() {

localStorage.removeItem("NomUtilisateur");
// window.location.href = "/";

}

function remplirnom() {
  var personne =localStorage.getItem("NomUtilisateur" );
  document.getElementsByName('createur')[0].value=personne;
}
