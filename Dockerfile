FROM mysql:latest

#Expose le port 3306 de mysql
EXPOSE 3306

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=root


# Copy the SQL script into the container
COPY bdd.sql /docker-entrypoint-initdb.d/

# Grant permissions to the script
RUN chmod +r /docker-entrypoint-initdb.d/bdd.sql

# Démarrer le serveur MySQL lors du lancement du conteneur
CMD ["mysqld"]
