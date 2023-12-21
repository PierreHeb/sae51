import mysql.connector

connection = mysql.connector.connect(
  host="10.0.119.89",
  port="3306",
  user="root",
  password="root",
  database="sae51"

)

cursor = connection.cursor()


def exercice1(connection):

  sql_select = "SELECT * FROM Ordinateurs WHERE marque='HP'"


  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les pc de la marque HP : {result}")



def exercice2(connection):
  sql_select = "SELECT * FROM Ordinateurs WHERE YEAR(date_achat)  BETWEEN '2018' and '2020'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC achetés entre 2018 et 2020 : {result}")



def exercice3(connection):
  sql_select = "SELECT * FROM Ordinateurs WHERE marque='HP' and YEAR(date_achat)  BETWEEN '2018' and '2020'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC achetés entre 2018 et 2020 de la marque HP: {result}")


def exercice4(connection):
  sql_select = "SELECT COUNT(*) FROM Ordinateurs WHERE marque = 'DELL'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici le nombre de pc de la marque DELL dans le parc: {result}")


def exercice5(connection):
  sql_select = "SELECT * FROM Ordinateurs WHERE ram BETWEEN '4' and '8'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici les pc qui ont entre 4 et 8 Go de RAM: {result}")


def exercice6(connection):
  sql_select = "SELECT nom_logiciel  FROM Logiciels INNER JOIN Ordinateurs ON Logiciels.id_ordinateur = Ordinateurs.id_ordinateur WHERE Ordinateurs.id_ordinateur ='5'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les logiciels installés sur la machine n°5: {result}")


def exercice7(connection):
  sql_select = "SELECT nom_logiciel FROM Logiciels INNER JOIN Utilisateurs ON Logiciels.id_ordinateur = Utilisateurs.id_ordinateur WHERE nom_utilisateur LIKE '%Summer%'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les logiciels installés sur la machine de Madame 'Summer': {result}")



def exercice8(connection):
  sql_select = "SELECT nom_logiciel FROM Logiciels INNER JOIN Utilisateurs ON Logiciels.id_ordinateur = Utilisateurs.id_ordinateur WHERE nom_utilisateur LIKE '%Summer%'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les logiciels installés sur la machine de Madame 'Summer': {result}")

def exercice9(connection):
  sql_select = "SELECT nom_utilisateur FROM Utilisateurs INNER JOIN Ordinateurs ON Utilisateurs.id_ordinateur = Ordinateurs.id_ordinateur WHERE Ordinateurs.systeme_exploitation LIKE 'Windows'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les utilisateurs utilisant une machine Windows: {result}")

def exercice9(connection):
  sql_select = "SELECT nom_utilisateur FROM Utilisateurs INNER JOIN Ordinateurs ON Utilisateurs.id_ordinateur = Ordinateurs.id_ordinateur WHERE Ordinateurs.systeme_exploitation LIKE 'Windows'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les utilisateurs utilisant une machine Windows: {result}")



def exercice9(connection):
  sql_select = "SELECT nom_utilisateur FROM Utilisateurs INNER JOIN Ordinateurs ON Utilisateurs.id_ordinateur = Ordinateurs.id_ordinateur WHERE Ordinateurs.systeme_exploitation LIKE 'Windows'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les utilisateurs utilisant une machine Windows: {result}")


def exercice10(connection):
  sql_select = "SELECT * FROM Ordinateurs INNER JOIN Maintenance ON Ordinateurs.id_ordinateur = Maintenance.id_ordinateur  WHERE Maintenance.date_maintenance  BETWEEN '2021-10-10' and '2021-12-10'"

  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC sur lesquels il y a eu une intervention entre le 10 Octobre et le 10 Décembre 2021: {result}")


def exercice11(connection):
  sql_select = "SELECT * FROM Ordinateurs INNER JOIN Maintenance ON Ordinateurs.id_ordinateur = Maintenance.id_ordinateur WHERE Maintenance.technicien LIKE '%Cooper%'"


  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC sur lesquel il y a eu une intervention en 2021 par le technicien Yolanda Cooper: {result}")


def exercice12(connection):
  sql_select = "SELECT * FROM Ordinateurs INNER JOIN Maintenance ON Ordinateurs.id_ordinateur = Maintenance.id_ordinateur WHERE Maintenance.technicien LIKE '%Cooper%' and YEAR(Maintenance.date_maintenance) = '2021'"


  cursor.execute(sql_select)
  result = cursor.fetchall()
  print(f"Voici tous les PC sur lesquel il y a eu une intervention en 2021 par le technicien Yolanda Cooper: {result}")






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
