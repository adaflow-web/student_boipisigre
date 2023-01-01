// initialisation des constantes

// le texte
const Letexte = document.getElementById('Letexte') ;

// la saisie
const Saisie = document.getElementById('Saisie') ;

// le button
const Action = document.getElementById("bu") ;

function remplir(){
  Letexte.innerHTML = Saisie.value;
}

Action.addEventListener("click", remplir);
