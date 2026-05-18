-- ========================================= -- PROYECTO INTEGRADOR - ACADEMIA DIGITAL -- =========================================

-- ========================================= -- PARTE 1 - CONSULTAS SQL -- =========================================

-- ========================================= -- CREACIÓN DE TABLAS -- =========================================

CREATE DATABASE IF NOT EXISTS academia_digital; USE academia_digital;

CREATE TABLE departamentos ( id INT PRIMARY KEY, nombre VARCHAR(100), presupuesto DECIMAL(10,2) );

CREATE TABLE empleados ( id INT PRIMARY KEY, nombre VARCHAR(100), salario DECIMAL(10,2), dept_id INT, FOREIGN KEY (dept_id) REFERENCES departamentos(id) );

CREATE TABLE proyectos ( id INT PRIMARY KEY, nombre VARCHAR(100), prioridad INT );

CREATE TABLE asignaciones ( empleado_id INT, proyecto_id INT, horas_dedicadas INT, PRIMARY KEY (empleado_id, proyecto_id), FOREIGN KEY (empleado_id) REFERENCES empleados(id), FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) );

-- ========================================= -- INSERTAR DATOS -- =========================================

INSERT INTO departamentos VALUES (1, 'Ventas', 50000.00), (2, 'Desarrollo', 120000.00), (3, 'Soporte', 35000.00), (4, 'RRHH', 45000.00);

INSERT INTO empleados VALUES (1, 'Ana Rojas', 3200.00, 1), (2, 'Luis Pérez', 4500.00, 1), (3, 'Diego Mora', 6000.00, 2), (4, 'Elena Solís', 5500.00, 2), (5, 'Mario Ruiz', 2500.00, 3), (6, 'Lucía Castro', 2800.00, 3), (7, 'Clara Soto', 3100.00, 4), (8, 'Roberto Vaca', 1500.00, NULL);

INSERT INTO proyectos VALUES (1, 'App Móvil V1', 10), (2, 'Mantenimiento Web', 5), (3, 'Migración Cloud', 9), (4, 'Seguridad Interna', 8);

INSERT INTO asignaciones VALUES (3, 1, 60), (4, 1, 50), (3, 3, 45), (1, 2, 20), (5, 2, 100);

-- ========================================= -- EJERCICIO 1 -- Promedio salarial por departamento -- =========================================

SELECT d.nombre AS departamento, AVG(e.salario) AS promedio_salarial FROM departamentos d JOIN empleados e ON d.id = e.dept_id GROUP BY d.nombre HAVING AVG(e.salario) > 3500;

-- ========================================= -- EJERCICIO 2 -- Clasificación de salarios -- =========================================

SELECT nombre, salario, CASE WHEN salario > 5000 THEN 'Senior' WHEN salario BETWEEN 3000 AND 5000 THEN 'Semi-Senior' ELSE 'Junior' END AS rango FROM empleados;

-- ========================================= -- EJERCICIO 3 -- Empleados sin asignaciones -- =========================================

SELECT e.nombre FROM empleados e LEFT JOIN asignaciones a ON e.id = a.empleado_id WHERE a.proyecto_id IS NULL;

-- ========================================= -- EJERCICIO 4 -- Bono por productividad -- =========================================

SELECT e.nombre, CASE WHEN SUM(a.horas_dedicadas) > 50 THEN e.salario * 0.10 ELSE 0 END AS bono FROM empleados e LEFT JOIN asignaciones a ON e.id = a.empleado_id GROUP BY e.id, e.nombre, e.salario;

-- ========================================= -- EJERCICIO 5 -- Departamentos con muchos empleados -- =========================================

SELECT d.nombre, COUNT(e.id) AS cantidad_empleados FROM departamentos d JOIN empleados e ON d.id = e.dept_id GROUP BY d.nombre HAVING COUNT(e.id) > 5;

-- ========================================= -- PARTE 2 -- SISTEMA DE CURSOS -- =========================================

-- ========================================= -- CREACIÓN DE TABLAS -- =========================================

CREATE TABLE categorias ( id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100) );

CREATE TABLE instructores ( id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), apellido VARCHAR(100), correo VARCHAR(100) );

CREATE TABLE cursos ( id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(150), precio DECIMAL(10,2), fecha_lanzamiento DATE, categoria_id INT, instructor_id INT, FOREIGN KEY (categoria_id) REFERENCES categorias(id), FOREIGN KEY (instructor_id) REFERENCES instructores(id) );

CREATE TABLE estudiantes ( id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), apellido VARCHAR(100), edad INT, fecha_registro DATE );

CREATE TABLE inscripciones ( estudiante_id INT, curso_id INT, fecha_inscripcion DATE, calificacion_final INT, PRIMARY KEY (estudiante_id, curso_id), FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id), FOREIGN KEY (curso_id) REFERENCES cursos(id) );

-- ========================================= -- INSERTAR DATOS -- =========================================

INSERT INTO categorias (nombre) VALUES ('Programación'), ('Diseño'), ('Marketing');

INSERT INTO instructores (nombre, apellido, correo) VALUES ('Carlos', 'Ramírez', 'carlos@gmail.com'), ('Laura', 'Méndez', 'laura@gmail.com'), ('José', 'Martínez', 'jose@gmail.com');

INSERT INTO cursos (titulo, precio, fecha_lanzamiento, categoria_id, instructor_id) VALUES ('MySQL Desde Cero', 100, '2025-01-10', 1, 1), ('Diseño UX', 120, '2025-02-15', 2, 2), ('Marketing Digital', 90, '2025-03-20', 3, 3), ('Java Avanzado', 150, '2025-04-05', 1, 1), ('Photoshop Profesional', 130, '2025-05-01', 2, 2);

INSERT INTO estudiantes (nombre, apellido, edad, fecha_registro) VALUES ('Ana', 'López', 20, '2025-01-01'), ('Luis', 'Pérez', 22, '2025-01-02'), ('María', 'Gómez', 21, '2025-01-03'), ('Pedro', 'Ruiz', 24, '2025-01-04'), ('Lucía', 'Castro', 19, '2025-01-05'), ('Mario', 'Soto', 23, '2025-01-06'), ('Elena', 'Vega', 20, '2025-01-07'), ('Clara', 'Morales', 22, '2025-01-08');

INSERT INTO inscripciones VALUES (1,1,'2025-06-01',85), (1,2,'2025-06-02',90), (2,1,'2025-06-03',70), (2,3,'2025-06-04',75), (3,2,'2025-06-05',88), (3,4,'2025-06-06',92), (4,1,'2025-06-07',60), (5,3,'2025-06-08',95), (6,4,'2025-06-09',80), (7,5,'2025-06-10',78), (8,2,'2025-06-11',82), (8,3,'2025-06-12',89);

-- ========================================= -- CONSULTA 1 -- Reporte de catálogo -- =========================================

SELECT c.titulo, cat.nombre AS categoria, CONCAT(i.nombre, ' ', i.apellido) AS instructor FROM cursos c JOIN categorias cat ON c.categoria_id = cat.id JOIN instructores i ON c.instructor_id = i.id;

-- ========================================= -- CONSULTA 2 -- Estudiantes por curso -- =========================================

SELECT c.titulo, CONCAT(e.nombre, ' ', e.apellido) AS estudiante FROM inscripciones ins JOIN cursos c ON ins.curso_id = c.id JOIN estudiantes e ON ins.estudiante_id = e.id WHERE c.titulo = 'MySQL Desde Cero';

-- ========================================= -- CONSULTA 3 -- Total de ingresos por curso -- =========================================

SELECT c.titulo, c.precio * COUNT(ins.estudiante_id) AS ingresos_totales FROM cursos c LEFT JOIN inscripciones ins ON c.id = ins.curso_id GROUP BY c.id, c.titulo, c.precio;

-- ========================================= -- CONSULTA 4 -- Promedio de estudiantes > 70 -- =========================================

SELECT CONCAT(e.nombre, ' ', e.apellido) AS estudiante, AVG(ins.calificacion_final) AS promedio FROM estudiantes e JOIN inscripciones ins ON e.id = ins.estudiante_id GROUP BY e.id, estudiante HAVING AVG(ins.calificacion_final) > 70;

-- ========================================= -- CONSULTA 5 -- Cursos sin alumnos -- =========================================

SELECT c.titulo FROM cursos c LEFT JOIN inscripciones ins ON c.id = ins.curso_id WHERE ins.estudiante_id IS NULL;

-- ========================================= -- CONSULTA 6 -- Cantidad de estudiantes por edad -- =========================================

SELECT edad, COUNT(*) AS cantidad_estudiantes FROM estudiantes GROUP BY edad ORDER BY cantidad_estudiantes DESC;