// initialisation des constantes

// le texte
const Lajout = document.getElementById('ajout');

// la saisie
const Saisie1 = document.getElementById('Saisie1') ;

// le button
const Action1 = document.getElementById("bu1") ;
const Action2 = document.getElementById("bu2") ;
const Action3 = document.getElementById("bu3") ;
// const Action4 = document.getElementById("bu4") ;

// déclaratuon des fonctions

function afficheTaches() {
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
}


function addTache(){
  const Newajout=document.createElement("p") ;

  Newajout.innerHTML = Saisie1.value;
  Newajout.className ="deco";

  Lajout.appendChild(Newajout);

  const textes = document.getElementsByClassName('deco') ;
  var numeroTache=textes.length-1;
  // ajout au localstorage
  localStorage.setItem(numeroTache,Saisie1.value)
  Saisie1.value ='Saisir une nouvelle Tache';
}

function removeTache(){

  const textes = document.getElementsByClassName('deco') ;

  if (textes.length > 0 ){
    var position = textes.length - 1;
    Lajout.removeChild(textes[position]);
    localStorage.removeItem(position);
  }
}

function clearTache(){
  const textes = document.getElementsByClassName('deco') ;
  i = textes.length-1;
  while ( i > -1 ) {
    Lajout.removeChild(textes[i]);
    localStorage.removeItem(i);
    i=i-1;
  }
}

// action des buttons
Action1.addEventListener("click", addTache);
Action2.addEventListener("click", removeTache);
Action3.addEventListener("click", clearTache);
// Action4.addEventListener("click", afficheTaches);
//
