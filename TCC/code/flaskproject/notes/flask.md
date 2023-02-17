# Déploiement site flask en production.

## Installation nginx
Sous debian :
> apt install nginx

Après avoir supprimer le serveur Apache.
> apt purge apache2

## Installation du code

### Installation de Git

> apt install git

### Import de clef SSH

création de la clef et import sur **gogs**
> ssh-keygen -t ed25519 -C "pib@pirboazo.net"

### Récupération du code

Pour cela on clone le repository distant par la commande
> git clone git@gogs.galicien.me:pboizot/microblog.git

## Installation de Flask
Sous root installation du paquet **python3-pip**
> apt install  python3-pip

puis des paquets pip **flask, flask-session, markdown**
> pip install flask-session  
> pip install markdown


## Mise en place d'un certificat auto-signé
### Installation openssl
> apt install openssl

### Création des certificats
Creating Self-Signed SSL Certificates for Apache | nginx on Linux [explications](https://www.linux.com/training-tutorials/creating-self-signed-ssl-certificates-apache-linux/)

> openssl req -new > new.cert.csr

donner un mot de passe et saisir toutes les information demander
>
> openssl rsa -in privkey.pem -out new.cert.key  
> openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key -days 1000

copie des certificats dans les répertoires ssl

> cp new.cert.cert /etc/ssl/certs/server.crt  
> cp new.cert.key /etc/ssl/private/server.key


### Paramétrage du proxy dans nginx
>
>
 server {  
    listen 443 ssl http2;

    server_name _;
    ssl_certificate /etc/ssl/certs/server.crt;
    ssl_certificate_key /etc/ssl/private/server.key;

        ssl_protocols TLSv1.2 TLSv1.1 TLSv1;

    location / {
        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Prefix /;
    }
    }


### Création du service Flask
La création d'un service qui relancera automatiquement l'application en cas de redémarrage de la machine ( serveur )

#### Description
Déclarer le fichier **flask.service** dans le répertoire **/etc/systemd/system**

#### Activation du service
> systemctl enable flask.service  
> systemctl start flask.service


## Mise à Jour de l'application (html, python)

La mise à jour se fait par le lancement d'un script sur la machine distante.
> ssh pboizot@192.168.56.101 -c /home/pboizot/app/bin/refresh.bash

Le script refresh.bash va chercher sur le repository distant les mises à jour, puis relance le service flask du serveur.

>
#!/usr/bin/bash
#
cd /home/pboizot/app/microblog

git  pull
echo $?
sudo systemctl restart flask.service

echo ' Mise a jour OK'
