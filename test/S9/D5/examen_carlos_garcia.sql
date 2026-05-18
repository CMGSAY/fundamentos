-- ====  PROYECTO INTEGRADOR  ACADEMIA DIGITAL  =====

-- ====  PARTE 1  CONSULTAS SQL  ====

-- ====  CREACIÓN DE TABLAS  ====

CREATE DATABASE academia_digital; 

USE academia_digital;

CREATE TABLE departamentos ( 
id INT PRIMARY KEY, 
nombre VARCHAR(100), 
presupuesto DECIMAL(10,2) 
);

CREATE TABLE empleados ( 
id INT PRIMARY KEY, 
nombre VARCHAR(100), 
salario DECIMAL(10,2), 
dept_id INT, 
FOREIGN KEY (dept_id) REFERENCES departamentos(id) 
);

CREATE TABLE proyectos ( 
id INT PRIMARY KEY, 
nombre VARCHAR(100), 
prioridad INT 
);

CREATE TABLE asignaciones ( 
empleado_id INT, 
proyecto_id INT, 
horas_dedicadas INT, 
PRIMARY KEY (empleado_id, proyecto_id), 
FOREIGN KEY (empleado_id) REFERENCES empleados(id), 
FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) 
);

CREATE TABLE inscripciones ( 
estudiante_id INT, 
curso_id INT, 
fecha_inscripcion DATE, 
calificacion_final INT, 
PRIMARY KEY (estudiante_id, curso_id), 
FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id), 
FOREIGN KEY (curso_id) REFERENCES cursos(id) );


-- ====  INSERTAR DATOS  ====

INSERT INTO departamentos VALUES 
(1, 'Ventas', 50000.00), 
(2, 'Desarrollo', 120000.00), 
(3, 'Soporte', 35000.00), 
(4, 'RRHH', 45000.00);

INSERT INTO empleados VALUES 
(1, 'Ana Rojas', 3200.00, 1), 
(2, 'Luis Pérez', 4500.00, 1), 
(3, 'Diego Mora', 6000.00, 2), 
(4, 'Elena Solís', 5500.00, 2), 
(5, 'Mario Ruiz', 2500.00, 3), 
(6, 'Lucía Castro', 2800.00, 3), 
(7, 'Clara Soto', 3100.00, 4), 
(8, 'Roberto Vaca', 1500.00, NULL);

INSERT INTO proyectos VALUES 
(1, 'App Móvil V1', 10), 
(2, 'Mantenimiento Web', 5), 
(3, 'Migración Cloud', 9), 
(4, 'Seguridad Interna', 8);

INSERT INTO asignaciones VALUES 
(3, 1, 60), 
(4, 1, 50), 
(3, 3, 45), 
(1, 2, 20), 
(5, 2, 100);


-- ==== EJERCICIO 1 ====

SELECT departamentos.nombre AS departamento, AVG(empleados.salario) AS promedio_salarial 
FROM departamentos  
JOIN empleados ON departamentos.id = empleados.dept_id 
GROUP BY departamentos.nombre 
HAVING AVG(empleados.salario) > 3500;

-- ====  EJERCICIO 2  ====

SELECT nombre, salario, 
CASE WHEN salario > 5000 THEN 'Senior' 
WHEN salario BETWEEN 3000 AND 5000 THEN 'Semi-Senior' 
ELSE 'Junior' END AS rango 
FROM empleados;

-- ====  EJERCICIO 3  ====

SELECT empleados.nombre 
FROM empleados  
LEFT JOIN asignaciones
ON empleados.id = asignaciones.empleado_id 
WHERE asignaciones.proyecto_id IS NULL;

-- ====  EJERCICIO 4 ====

SELECT empleados.nombre,
CASE WHEN SUM(asignaciones.horas_dedicadas) > 50 
THEN empleados.salario * 0.10 
ELSE 0 END AS bono 
FROM empleados
LEFT JOIN asignaciones 
ON empleados.id = asignaciones.empleado_id 
GROUP BY empleados.id, empleados.nombre, empleados.salario;

-- ==== EJERCICIO 5 ====

SELECT departamentos.nombre, COUNT(empleados.id) AS cantidad_empleados 
FROM departamentos 
JOIN empleados ON departamentos.id = empleados.dept_id 
GROUP BY departamentos.nombre 
HAVING COUNT(empleados.id) > 5;





-- ====  PARTE 2  ====

-- ====  1 CREACIÓN DE TABLAS   ====

CREATE TABLE categorias ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
nombre VARCHAR(100) 
);

CREATE TABLE instructores ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
nombre VARCHAR(100), 
apellido VARCHAR(100),
correo VARCHAR(100) 
);

CREATE TABLE cursos ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
titulo VARCHAR(150), 
precio DECIMAL(10,2), 
fecha_lanzamiento DATE, 
categoria_id INT, 
instructor_id INT, 
FOREIGN KEY (categoria_id) REFERENCES categorias(id), 
FOREIGN KEY (instructor_id) REFERENCES instructores(id) 
);

CREATE TABLE estudiantes ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
nombre VARCHAR(100), 
apellido VARCHAR(100), 
edad INT, 
fecha_registro DATE 
);

CREATE TABLE inscripciones ( 
estudiante_id INT, 
curso_id INT, 
fecha_inscripcion DATE, 
calificacion_final INT, 
PRIMARY KEY (estudiante_id, curso_id), 
FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
FOREIGN KEY (curso_id) REFERENCES cursos(id) 
 );


-- ==== 2 INSERTAR DATOS  ====

INSERT INTO categorias (nombre) VALUES
 ('Programación'), 
 ('Diseño'), 
 ('Marketing');

INSERT INTO instructores (nombre, apellido, correo) VALUES 
('Carlos', 'García', 'carlos@gmail.com'), 
('Eunice', 'Hernández', 'eunice@gmail.com'), 
('Juan', 'Casia', 'juan@gmail.com');

INSERT INTO cursos (titulo, precio, fecha_lanzamiento, categoria_id, instructor_id) VALUES 
('MySQL Desde Cero', 100, '2025-01-08', 1, 1), 
('Python Desde Cero', 120, '2025-01-15', 2, 2), 
('Marketing Digital', 90, '2025-02-20', 3, 3), 
('Java Avanzado', 150, '2025-03-05', 1, 1), 
('Photoshop Principiantes', 130, '2025-03-09', 2, 2);

INSERT INTO estudiantes (nombre, apellido, edad, fecha_registro) VALUES 
('Erickson', 'López', 20, '2026-01-08'), 
('Esdras', 'Pérez', 22, '2026-02-08'), 
('Paul', 'Gómez', 21, '2026-02-09'), 
('Carlos', 'Ruiz', 24, '2026-02-09'), 
('Luigi', 'Castro', 19, '2026-02-10'), 
('Mario', 'Castro', 23, '2026-02-10'), 
('Luis', 'Velázques', 20, '2026-02-11'), 
('Cristian', 'Yat', 22, '2026-02-14');

INSERT INTO inscripciones VALUES 
(1,1,'2026-02-25',85), 
(1,2,'2026-02-25',90), 
(2,1,'2026-02-25',70), 
(2,3,'2026-02-25',75), 
(3,2,'2026-02-26',88), 
(3,4,'2026-02-26',92), 
(4,1,'2026-02-26',60), 
(5,3,'2026-02-26',95), 
(6,4,'2026-02-27',80), 
(7,5,'2026-02-27',78), 
(8,2,'2026-02-28',82), 
(8,3,'2026-02-28',89);


-- ==== Consultas ====
-- ==== EJERCICIO 1 ====

SELECT cursos.titulo, categorias.nombre, 
CONCAT(instructores.nombre, ' ', instructores.apellido) AS Instructor
FROM cursos
JOIN categorias
ON cursos.categoria_id = categorias.id 
JOIN instructores ON cursos.instructor_id = instructores.id;


-- ==== EJERCICIO 2 ====
SELECT cursos.titulo, CONCAT(estudiantes.nombre, ' ', estudiantes.apellido) AS estudiante 
FROM inscripciones  
JOIN cursos ON inscripciones.curso_id = cursos.id 
JOIN estudiantes ON inscripciones.estudiante_id = estudiantes.id 
WHERE cursos.titulo = 'MySQL Desde Cero';


-- ==== EJERCICIO 3 ====
SELECT cursos.titulo, cursos.precio * COUNT(inscripciones.estudiante_id) AS ingresos_totales 
FROM cursos  
LEFT JOIN inscripciones ON cursos.id = inscripciones.curso_id 
GROUP BY cursos.id, cursos.titulo, cursos.precio;


-- ==== EJERCICIO 4 ====
SELECT CONCAT(estudiantes.nombre, ' ', estudiantes.apellido) AS estudiante, AVG(inscripciones.calificacion_final) AS promedio 
FROM estudiantes 
JOIN inscripciones  ON estudiantes.id = inscripciones.estudiante_id 
GROUP BY estudiantes.id, estudiante 
HAVING AVG(inscripciones.calificacion_final) > 70;


-- ==== EJERCICIO 5 ====
SELECT cursos.titulo 
FROM cursos  
LEFT JOIN inscripciones  ON cursos.id = inscripciones.curso_id
WHERE inscripciones.estudiante_id IS NULL;


-- ==== EJERCICIO 6 ====
SELECT edad, COUNT(*) AS cantidad_estudiantes 
FROM estudiantes 
GROUP BY edad 
ORDER BY cantidad_estudiantes DESC;