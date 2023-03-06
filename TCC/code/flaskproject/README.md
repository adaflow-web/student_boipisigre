## Introduction

Ce répertoire est dédié aux applications développées avec le Framework [Flask](https://flask.palletsprojects.com/)

## Installation de Flask

Flask est installé dans un environnement virtuel géré avec [pipenv](https://pipenv.pypa.io/en/latest/index.html).

Pipienv doit être installé préalablement avec pip ou un package suivant votre environnement.

**Linux Debian**

   >apt install pipenv

**Windows**
> pip install pipenv

ensuite installer par la commande
> pipenv shell   
pipenv install Flask

Un fichier requirements.txt a été ajouté pour facilité l'installation des modules.


on crera un répertoire par application avec les sous - rpertoires
   * static : pour les fichiers css, js, images
   * template : pour les fichiers templates

## Gestion de l'environnement.

on rentre dans l'environnement en se positionnant dans le répertoire où on a installé flask avec pipenv.

vous pouvez vérifier que c'est le bon environnement par la commande:

**pipenv graph**

> Flask==2.2.2
  - click [required: >=8.0, installed: 8.1.3]
  - importlib-metadata [required: >=3.6.0, installed: 6.0.0]
    - zipp [required: >=0.5, installed: 3.11.0]
  - itsdangerous [required: >=2.0, installed: 2.1.2]
  - Jinja2 [required: >=3.0, installed: 3.1.2]
    - MarkupSafe [required: >=2.0, installed: 2.1.1]
  - Werkzeug [required: >=2.2.2, installed: 2.2.2]
    - MarkupSafe [required: >=2.1.1, installed: 2.1.1]
pkg-resources==0.0.0

## Exécution de flask

Descendre dans un projet et lancer le ficher lancer.bash
dont voici un exemple pour l'~application~ exercice param
> export FLASK_APP=param
flask run
