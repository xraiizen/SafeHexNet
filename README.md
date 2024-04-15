# Projet de Communication de Données
Ce projet permet d'envoyer et de recevoir des données sécurisées entre un client et un serveur sur le réseau local (localhost) en utilisant le protocole TCP. Les données sont encodées en hexadécimal et incluent un checksum pour vérifier l'intégrité des données à la réception.

## Fonctionnalités
Encodage en Hexadécimal : Les données sont converties en format hexadécimal avant l'envoi.
Checksum MD5 : Un checksum MD5 est calculé et envoyé avec les données pour permettre la vérification de l'intégrité à la réception.
Communication via Socket TCP : Utilise les sockets TCP pour une communication de point à point.

## Installation
Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :

``` bash
git clone https://github.com/xraiizen/SafeHexNet
```
Naviguez dans le répertoire du projet :

``` bash
cd ./SafeHexNet
```
## Usage
Pour démarrer le serveur, ouvrez un terminal et exécutez :

``` bash
python server.py
```

Le serveur commencera à écouter sur le port spécifié (par défaut 65432). Pour envoyer des données, ouvrez un second terminal et exécutez :

``` bash
python client.py
```
Le script client enverra des données prédéfinies au serveur, qui vérifiera l'intégrité des données reçues et affichera le résultat.

## Configuration
Vous pouvez configurer le port et l'adresse IP du serveur en modifiant les paramètres dans les scripts server.py et client.py.

Sécurité
Ce projet est destiné à des fins de démonstration et ne doit pas être utilisé tel quel pour des communications sécurisées dans un environnement de production. Pour améliorer la sécurité, envisagez d'utiliser des mécanismes de chiffrement et d'authentification plus robustes.

Licence
Ce projet est distribué sous la licence MIT.
