
-- Creation de la DATABASE
CREATE DATABASE IF NOT EXISTS sae51;

USE sae51;
-- Table pour stocker les informations sur chaque ordinateur
CREATE TABLE Ordinateurs (
    id_ordinateur INT PRIMARY KEY,
    configuration_materielle VARCHAR(255),
    systeme_exploitation VARCHAR(255),
    marque VARCHAR(50),
    date_achat DATE,
    ram INT
);

-- Table pour suivre les logiciels installés sur chaque ordinateur
CREATE TABLE Logiciels (
    id_logiciel INT PRIMARY KEY,
    nom_logiciel VARCHAR(255),
    version VARCHAR(50),
    licence VARCHAR(50),
    id_ordinateur INT,
    FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id_ordinateur)
);

-- Table pour enregistrer les utilisateurs associés à chaque ordinateur
CREATE TABLE Utilisateurs (
    id_utilisateur INT PRIMARY KEY,
    nom_utilisateur VARCHAR(100),
    id_ordinateur INT,
    FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id_ordinateur)
);

-- Table pour enregistrer les affectations des utilisateurs aux ordinateurs
CREATE TABLE Affectations (
    id_affectation INT PRIMARY KEY,
    id_utilisateur INT,
    id_ordinateur INT,
    date_affectation DATE,
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id_utilisateur),
    FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id_ordinateur)
);

-- Table pour gérer les problèmes de maintenance
CREATE TABLE Maintenance (
    id_maintenance INT PRIMARY KEY,
    id_ordinateur INT,
    date_maintenance DATE,
    action_effectuee VARCHAR(255),
    technicien VARCHAR(100),
    -- Ajoutez d'autres colonnes nécessaires pour les détails de la maintenance
    FOREIGN KEY (id_ordinateur) REFERENCES Ordinateurs(id_ordinateur)
);
