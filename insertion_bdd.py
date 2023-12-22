import csv
import asyncio
import mysql.connector


connection = mysql.connector.connect(
  host="10.0.119.137",
  port="3306",
  user="root",
  password="root",
  database="sae51"

)


#Fonction générale d'insertion des données
def insertion_csvto_sql(fichier_csv, nom_table, connection_bdd):
    with open(fichier_csv,'r',encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader) # Ignorer les en-têtes
        sql_insertion = f"INSERT INTO {nom_table} ({','.join(headers)}) VALUES "
        for row in csv_reader: #Itère sur le nombre de ligne du csv
            values_row = ",".join([f"{row}"]) # Ajoute les élements dans un str
            sql_insertion += f"{values_row}, ".replace('[','(').replace(']',')')

        cursor = connection.cursor()
        cursor.execute(sql_insertion[:-2]) #On exécute la commande en retirant la virgule de fin et l'espace possible qui ont été générée
        connection.commit()
        cursor.close()

        print(sql_insertion)




insertion_csvto_sql("ordinateurs.csv","Ordinateurs", connection)
insertion_csvto_sql("logiciels.csv","Logiciels", connection)
insertion_csvto_sql("utilisateurs.csv","Utilisateurs", connection)
insertion_csvto_sql("maintenance.csv","Maintenance", connection)
insertion_csvto_sql("affectations.csv","Affectations", connection)

