
function lirenom() {
//  console.log(localStorage.length) ;
// if (localStorage.length> 0) {
if (localStorage.length >0) {
for (let key=0 ; key < localStorage.length; key++){
     var tache=localStorage.getItem(key);
     const Newajout=document.createElement("p") ;
     Newajout.innerHTML = tache;
     Newajout.className ="deco";
     Lajout.appendChild(Newajout);
   }
 }
else {
  let person = prompt("Please enter your name", "Harry Potter");
  if (person != null) {
    document.getElementById("name").innerHTML = "Hello " + person + "! How are you today?";
  }
}
}
