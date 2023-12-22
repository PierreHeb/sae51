import mysql.connector

connection = mysql.connector.connect(
  host="10.0.119.137",
  port="3306",
  user="root",
  password="root",
  database="sae51"

)

cursor = connection.cursor()

#liste de toutes machines de marque HP
def exercice1(connection):

  sql_select = "SELECT * FROM Ordinateurs WHERE marque='HP'"


  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les pc de la marque HP : {result}")


#liste de toutes les machines achetées entre 2018 et 2020
def exercice2(connection):
  sql_select = "SELECT * FROM Ordinateurs WHERE YEAR(date_achat)  BETWEEN '2018' and '2020'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC achetés entre 2018 et 2020 : {result}")


#liste de toutes machines de marque HP achetées entre 2019 et 2020
def exercice3(connection):
  sql_select = "SELECT * FROM Ordinateurs WHERE marque='HP' and YEAR(date_achat)  BETWEEN '2018' and '2020'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC achetés entre 2018 et 2020 de la marque HP: {result}")

#Nombre de machines de marque Dell dans l’ensemble du parc
def exercice4(connection):
  sql_select = "SELECT COUNT(*) FROM Ordinateurs WHERE marque = 'DELL'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici le nombre de pc de la marque DELL dans le parc: {result}")

#liste de toutes machines ayant entre 4GB et 8GB de RAM
def exercice5(connection):
  sql_select = "SELECT * FROM Ordinateurs WHERE ram BETWEEN '4' and '8'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici les pc qui ont entre 4 et 8 Go de RAM: {result}")

#liste des logiciels installés sur la machine n°1234
def exercice6(connection):
  choice = input("Veuillez choisir le numéro de la machine dont vous voulez connaitre les logiciels installés : ")
  sql_select = f"SELECT nom_logiciel  FROM Logiciels INNER JOIN Ordinateurs ON Logiciels.id_ordinateur = Ordinateurs.id_ordinateur WHERE Ordinateurs.id_ordinateur ='{choice}'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les logiciels installés sur la machine n°{choice}: {result}")

#liste des logiciels installés sur la machine attribuée à M. Duchmoll
def exercice7(connection):
  choice = input("Veuillez choisir le nom de la personne dont vous souhaitez connaitre les logiciels installés sur sa machine : ")
  sql_select = f"SELECT nom_logiciel FROM Logiciels INNER JOIN Utilisateurs ON Logiciels.id_ordinateur = Utilisateurs.id_ordinateur WHERE nom_utilisateur LIKE '%{choice}%'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les logiciels installés sur la machine de l'utilisateur {choice}: {result}")


#liste des utilisateurs utilisant une machine de marque HP
def exercice8(connection):
  sql_select = "SELECT nom_utilisateur FROM Utilisateurs INNER JOIN Ordinateurs ON Utilisateurs.id_ordinateur = Ordinateurs.id_ordinateur WHERE Ordinateurs.marque LIKE 'HP'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les utilisateurs utilisant une machine de marque HP : {result}")

#liste des utilisateurs utilisant une machine de marque HP avec un OS "Windows 10"
def exercice9(connection):
  sql_select = "SELECT nom_utilisateur FROM Utilisateurs INNER JOIN Ordinateurs ON Utilisateurs.id_ordinateur = Ordinateurs.id_ordinateur WHERE Ordinateurs.systeme_exploitation LIKE 'Windows'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les utilisateurs utilisant une machine Windows: {result}")


#liste des machines sur lesquelles il y a eu intervention technique entre le 10/10/2021 et le 10/12/2021
def exercice10(connection):
  sql_select = "SELECT * FROM Ordinateurs INNER JOIN Maintenance ON Ordinateurs.id_ordinateur = Maintenance.id_ordinateur  WHERE Maintenance.date_maintenance  BETWEEN '2021-10-10' and '2021-12-10'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC sur lesquels il y a eu une intervention entre le 10 Octobre et le 10 Décembre 2021: {result}")

#liste de machines sur lesquelles le technicien Jean Neymar a fait de la maintenance
def exercice11(connection):
  choice = input("Veuillez choisir le nom du technicien dont vous souhaitez connaitre la machine sur laquelle il est intervenu : ")
  sql_select = f"SELECT * FROM Ordinateurs INNER JOIN Maintenance ON Ordinateurs.id_ordinateur = Maintenance.id_ordinateur WHERE Maintenance.technicien LIKE '%{choice}%'"


  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC sur lesquel il y a eu une intervention en 2021 par le technicien {choice}: {result}")

#liste de machines sur lesquelles le technicien Jean Neymar a fait de la maintenance en 2021
def exercice12(connection):
  choice = input("Veuillez choisir le nom du technicien dont vous souhaitez connaitre la ou les machines sur lesquelles il est intervenu : ")
  sql_select = f"SELECT * FROM Ordinateurs INNER JOIN Maintenance ON Ordinateurs.id_ordinateur = Maintenance.id_ordinateur WHERE Maintenance.technicien LIKE '%{choice}%' and YEAR(Maintenance.date_maintenance) = '2021'"


  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC sur lesquel il y a eu une intervention en 2021 par le technicien {choice}: {result}")



choice = input("Choisissez un numéro d'exercice entre  1 et 12 pour la selection sql :")

selected_exercise = f"exercice{choice}"

globals()[selected_exercise](connection)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
