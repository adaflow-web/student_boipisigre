// initialisation des constantes

// le texte
const Letexte = document.getElementById('Letexte') ;

// la saisie
const Saisie = document.getElementById('Saisie') ;

// le button
const Action = document.getElementById("bu") ;

function remplir(){
  Letexte.innerHTML = Saisie.value+"<br>";
  Saisie.value ='un autre texte'
}

Action.addEventListener("click", remplir);
Action.addEventListener("dblclick", function(){
  document.getElementById("Letexte").innerHTML = "........";
}
)
