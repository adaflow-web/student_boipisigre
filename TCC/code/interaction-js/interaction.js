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
const Action3 = document.getElementById("bu3") ;
const Action4 = document.getElementById("bu4") ;

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

function remove1(){

  const textes = document.getElementsByClassName('deco') ;

  if (textes.length > 0 ){
    Lajout.removeChild(textes[0])
  }
}

function remove2(){

  const textes = document.getElementsByClassName('deco') ;

  if (textes.length > 0 ){
    var position = textes.length - 1;
    Lajout.removeChild(textes[position]);
  }
}

Action1.addEventListener("click", remplir);
Action1.addEventListener("dblclick", function(){
  document.getElementById("Letexte").innerHTML = "........";
}
)

Action2.addEventListener("click", addtext);

Action3.addEventListener("click", remove1);

Action4.addEventListener("click", remove2);
