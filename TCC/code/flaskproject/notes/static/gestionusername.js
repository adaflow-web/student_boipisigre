
function lirenom() {
//  console.log(localStorage.length) ;
// if (localStorage.length> 0) {
if (localStorage.length >0) {
  var key="NomUtilisateur" ;
  var personne =localStorage.getItem(key);
  document.getElementById("name").innerHTML = ""  + personne;
   }
else {
  let personne = prompt("Bonvolu skribas vian nomon", "Zamenov");
  if (personne != null) {
    document.getElementById("name").innerHTML = ""+ personne ;
    localStorage.setItem("NomUtilisateur",personne);
  }
}
}

function clearnom() {

localStorage.removeItem("NomUtilisateur");
window.location.href = "/";

}
