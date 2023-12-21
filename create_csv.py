from faker import Faker
import random
from datetime import date, timedelta
import csv


fake = Faker()


#Ici, on génère différentes données des ordinateurs
def gener_pc(id_ordinateur):
  marques = ["HP", "Dell", "Lenovo", "Asus"]
  processor = fake.random_element(elements=("Intel Core i7", "AMD Ryzen 5", "Intel Core i5", "AMD Ryzen 7"))
  ram_size = fake.random_element(elements=(8, 16, 32, 64))
  storage = fake.random_element(elements=("SSD", "HDD"))
  storage_size = fake.random_element(elements=("256GB", "512GB", "1TB", "2TB"))

  description = f"Configuration materielle : {processor}, {ram_size}GB RAM, {storage_size} {storage}"
  print(description)

  return [
    description,
    fake.random_element(elements=("Windows", "Linux", "Mac")), #OS
    fake.random_element(elements=marques), #Marques
    fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d"), #Date d'achat
    ram_size, #RAM
    id_ordinateur
  ]

#Ici, on génère différentes données des logiciels
def gener_logiciels(id_ordianteur,id_logiciels):
    noms_logiciels = ["Firefox", "Word", "Excel", "PowerPoint", "Photoshop", "Illustrator", "Pycharm"]
    noms_licence = ["Office", "Adobe"]
    logiciels = fake.random_choices(elements=noms_logiciels, length=2)

    return [
      logiciels, #Logiciels
      fake.random_number(digits=3),#Version
      fake.random_element(elements=noms_licence),
      id_ordianteur,
      id_logiciels
    ]

#Ici, on génère les noms des utilisateurs
def generate_utilisateur_data(id_utilisateur,id_ordinateur):
  return [
    fake.name(),  # nom_utilisateur
    id_utilisateur,
    id_ordinateur
  ]

#Ici, on génère les dates d'affectations des ordinateurs
def generate_affectation_data(id_affectation,id_utilisateur,id_ordinateur):
    return [
      fake.date_between(start_date='-10y', end_date='today').strftime("%Y-%m-%d"),  # date_affectation de l'utilisateur
      id_affectation,
      id_utilisateur,
      id_ordinateur
    ]

#Ici, on génère les données des dates de maintenance
def generate_maintenance_data(id_maintenance,id_ordinateur):
    return [
        fake.date_between(start_date='-10y', end_date='today').strftime("%Y-%m-%d"),  # date_maintenance de l'ordinateur
        fake.sentence(),  # action effectuee
        fake.name(),  # nom du technicien
        id_maintenance,
        id_ordinateur
    ]





#Définition des en-têtes de chaque csv pour que cela soit plus lisible lors de l'ouverture du csv
ordinateurs_columns = ["configuration_materielle", "systeme_exploitation", "marque", "date_achat", "ram","id_ordinateur"]
logiciels_columns = ["nom_logiciel", "version", "licence","id_logiciel","id_ordinateur"]
utilisateur_columns = ["nom_utilisateur","id_utilisateur","id_ordinateur"]
maintenance_columns = ["date_maintenance", "action_effectuee", "technicien","id_maintenance","id_ordinateur"]
affectations_columns = ["date_affectation","id_affectation","id_utilisateur","id_ordinateur"]

#On ouvre chaque CSV et on écrit les en-têtes
with open(f'ordinateurs.csv','a',newline='',encoding='utf-8') as pc_csv:
    writer = csv.writer(pc_csv)
    writer.writerow(ordinateurs_columns)

with open(f'logiciels.csv', 'a', newline='', encoding='utf-8') as logiciels_csv:
    writer = csv.writer(logiciels_csv)
    writer.writerow(logiciels_columns)

with open(f'utilisateurs.csv', 'a', newline='', encoding='utf-8') as utilisateur_csv:
    writer = csv.writer(utilisateur_csv)
    writer.writerow(utilisateur_columns)

with open(f'maintenance.csv', 'a', newline='', encoding='utf-8') as maintenance_csv:
    writer = csv.writer(maintenance_csv)
    writer.writerow(maintenance_columns)

with open(f'affectations.csv', 'a', newline='', encoding='utf-8') as affect_csv:
    writer = csv.writer(affect_csv)
    writer.writerow(affectations_columns)




j=0
#Insertion des données dans les csv
for i in range(2,10):
  j+=1
  with open(f'ordinateurs.csv','a',newline='',encoding='utf-8') as pc_csv:
    writer = csv.writer(pc_csv)
    writer.writerow(gener_pc(id_ordinateur=j))

  with open(f'logiciels.csv', 'a', newline='', encoding='utf-8') as logiciels_csv:
    writer = csv.writer(logiciels_csv)
    writer.writerow(gener_logiciels(id_logiciels=j,id_ordianteur=j))

  with open(f'utilisateurs.csv', 'a', newline='', encoding='utf-8') as utilisateur_csv:
    writer = csv.writer(utilisateur_csv)
    writer.writerow(generate_utilisateur_data(id_ordinateur=j,id_utilisateur=j))


  with open(f'maintenance.csv', 'a', newline='', encoding='utf-8') as maintenance_csv:
    writer = csv.writer(maintenance_csv)
    writer.writerow(generate_maintenance_data(id_maintenance=j,id_ordinateur=j))

  with open(f'affectations.csv', 'a', newline='', encoding='utf-8') as affect_csv:
      writer = csv.writer(affect_csv)
      writer.writerow(generate_affectation_data(id_ordinateur=j,id_utilisateur=j,id_affectation=j))

