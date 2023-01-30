
function lirenom() {
//  console.log(localStorage.length) ;
// if (localStorage.length> 0) {
if (localStorage.length >0) {

  var personne =localStorage.getItem("NomUtilisateur" );
  document.getElementById("name").innerHTML = ""  + personne;
   }
else {
  let personne = prompt("Bonvolu skribas vian nomon", "Zamenov");
  if (personne != null) {
    // document.getElementById("name").innerHTML = ""+ personne ;
    localStorage.setItem("NomUtilisateur",personne);
  }
  if (personne == "") {
    // document.getElementById("name").innerHTML = ""+ personne ;
    localStorage.removeItem("NomUtilisateur");
  }
  window.location.href = "/";
}
}

function clearnom() {

localStorage.removeItem("NomUtilisateur");
window.location.href = "/";

}

function remplirnom() {
  var personne =localStorage.getItem("NomUtilisateur" );
  document.getElementsByName('createur')[0].value=personne;
}
