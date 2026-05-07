DROP TABLE IF EXISTS inscripciones;
DROP TABLE IF EXISTS estudiantes;
DROP TABLE IF EXISTS cursos;

CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
);

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(50),
    precio DECIMAL(10,2)
);

CREATE TABLE inscripciones (
    estudiante_id INT,
    curso_id INT,
    nota INT,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

INSERT INTO estudiantes (nombre, edad) VALUES ('Juan', 20), ('Maria', 25), ('Luis', 30), ('Ana', 22);
INSERT INTO cursos (nombre_curso, precio) VALUES ('SQL', 100.00), ('Java', 150.00), ('Python', 120.00);
INSERT INTO inscripciones VALUES (1, 1, 85), (1, 2, 90), (2, 1, 70), (3, 3, 95), (4, 1, 100), (2, 3, 88);