## lien sur le descriptif de l'application
[analyse]( https://pad.monuage.ch/code/#/2/code/view/BHfzGxFgaLHxSguU+wKWPg-+oiqmXfVb7206CQA+KN0/)

## Ouverture d'une branch sqlite.

je vais basculer la gestion des notes d'un fichiers texte vers une base sqlite

la structure de la table est :
  titre char(50),
  corps text

Conséquence les fonction d'accédant aux données doivent être modifié:
* add_notes(texte) **la première version doit être modifié** pour prendre deux parametre au lieu de un
* get_notes()  
