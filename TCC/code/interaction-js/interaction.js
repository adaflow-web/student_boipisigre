// initialisation des constantes

// le texte
const Letexte = document.getElementById('Letexte') ;
const Lajout = document.getElementById('ajout');

// la saisie
const Saisie1 = document.getElementById('Saisie1') ;
const Saisie2 = document.getElementById('Saisie2') ;

// le button
const Action1 = document.getElementById("bu1") ;

const Action2 = document.getElementById("bu2") ;

function remplir(){
  Letexte.innerHTML = Saisie1.value+"<br>";
  Saisie1.value ='changer le texte'
}

function addtext(){
  const Newajout=document.createElement("p") ;
  Newajout.innerHTML = Saisie2.value +"<br>";
  Newajout.className ="deco";

  Lajout.appendChild(Newajout);
  Saisie2.value ='le texte NOUVEAU';
}

Action1.addEventListener("click", remplir);
Action1.addEventListener("dblclick", function(){
  document.getElementById("Letexte").innerHTML = "........";
}
)

Action2.addEventListener("click", addtext);
