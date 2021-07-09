CREATE DATABASE final_OS;
USE final_OS;

CREATE TABLE leads(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255),
    telefono varchar(255),
    fecha DATE,
    ciudad VARCHAR(255),
    id_productor INTEGER,
    fecha_inicio timestamp,
    PRIMARY KEY(id)
);

CREATE TABLE compradores(
    id INTEGER NOT NULL AUTO_INCREMENT,
    id_lead INTEGER,
    comprador VARCHAR(255),
    precio VARCHAR(255),
    fecha_inicio timestamp,
    PRIMARY KEY(id),
    FOREIGN KEY(id_lead) REFERENCES leads(id)
);

    