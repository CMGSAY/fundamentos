-- Crear la base de datos
CREATE DATABASE estacion_eathelgard;

-- Usar la base de datos
USE estacion_eathelgard;

-- Crear la tabla Flota
CREATE TABLE flota(
id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(50),
clase VARCHAR(10),
energia INT,
escudo INT,
UNIQUE (id),
PRIMARY KEY (id) 
);

-- Registrar datos a la tabla
INSERT INTO flota(nombre, clase, energia, escudo) VALUE(
'Centinela-X', 'Combate', 100, 100);

INSERT INTO flota(nombre, clase, energia, escudo) VALUE(
'Carguero-01', 'Carga',  80, 100);

INSERT INTO flota(nombre, clase, energia, escudo) VALUE(
'Titan-Alpha', 'Híbrida',  90, 50);

-- Modificar Energia
UPDATE flota SET energia = 50 WHERE nombre = 'Centinela-X';

-- Reforzar Escudo
UPDATE flota SET escudo = 100 WHERE nombre = 'Titan-Alpha';

-- Baja de Servicios
DELETE FROM flota WHERE nombre = 'Carguero-01';

