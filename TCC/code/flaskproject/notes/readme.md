## Descriptif de l'application
[analyse]( https://pad.monuage.ch/code/#/2/code/view/BHfzGxFgaLHxSguU+wKWPg-+oiqmXfVb7206CQA+KN0/)


## Amélioration

* Creation d'une branche sqlite pour migrer de fichier txt vers db ssqlite
* creation d'une branche jinja pour améliorer le html et utiliser les templates surt la base de la gestion en fichier...

## Ouverture d'une branch sqlite.

Bascule de la gestion des notes d'un fichiers texte vers une base sqlite

la structure de la table est :
  titre char(50),
  corps text

Conséquence les fonction d'accédant aux données doivent être modifié:

* add_notes(texte) **la première version doit être modifié** pour prendre deux parametre au lieu de un
* get_notes()  

* les codes
  * champs=note.split("€") --> champs=note[0].split("€")
  * champs=unenote.split("€") --> champs=unenote[0].split("€")

## Ouverture d'une branche jinja.

Cette branch a été créé à partir de  la branch main :-(

Premier test avec jinja

## merge des branche sqlite et jinja2

Il y a des conflits à gérer manuellement.

## Creation de la branche cssv1
Pour intégrer Bulma

## creation de la version V1
finaliser L'ntégration avec sqlite et jinja2

## creation de la version V2

pour filtrage sur le NomUtilisateur

## creation Version 4
Ajouter du hash du mot de passe

## version 5
Ajout menu dropdown ;-)
Ajout du suivi sur la page de l'application
