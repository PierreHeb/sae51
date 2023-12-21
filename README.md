# sae51
# Utilisation des différents scripts

 Pour commencer, lancez le script "launch.sh" afin de créer l'image ainsi que le conteneur docker mysql qui contiendra la base de données générées par le fichir bdd.sql
Une fois lancé, vous devrez mettre en place votre environnement python en utilisant le fichier "requirements.txt" qui contient toutes les bibliothèques à installer.

## Utilisation des scripts python
Une fois votre environnement établi, il ne vous reste plus qu'à lancer les différents scripts .py qui se trouvent dans ce dossier.
Dans l'ordre :
  - creation_csv.py : va générer les différents fichiers csv
  - insertion_sql.py : qui va injecter les données des csv dans la base de données sql
  - selection.py : qui va générer les différentes requêtes sql demandés
