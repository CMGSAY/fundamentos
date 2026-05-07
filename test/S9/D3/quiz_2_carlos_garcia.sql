-- 1. El club de los identificados (Relacion 1 a 1)
SELECT usuario.name, identificacion.dni_number
FROM users AS usuario
INNER JOIN dni AS identificacion
ON usuario.user_id = identificacion.user_id;


-- Directorio empresarial (Relacion 1 a muchos)
SELECT usuario.name AS nombre_usuario, empresa.name AS nombre_empresa
FROM users AS usuario
INNER JOIN companies AS empresa
ON usuario.company_id = empresa.company_id;

-- 3. Analisis de inclusion Laboral ( Relacion 1: muchos con NULL)
SELECT usuario.name AS nombre_usuario, empresa.name AS nombre_empresa
FROM users AS usuario
LEFT JOIN companies AS empresa
ON usuario.company_id = empresa.company_id;

--4 Iventario de Habilidades (relacion muchos a muchos)
SELECT usuario.name AS nombre_usuario, lenguaje.name AS nombre_lenguaje
FROM users AS usuario
INNER JOIN users_lenguajes AS usuario_lenguajes
ON usuario.user_id = usuario_lenguajes.user_id
INNER JOIN lenguajes AS lenguaje
ON usuario_lenguajes.lenguaje_id = lenguaje.lenguaje_id;

-- 5. Reporte de Popularidad de lenguajes (Relacion muchos a muchos Avanzada)
SELECT lenguaje.name AS nombre_lenguaje, usuario.name AS nombre_usuario
FROM lenguajes AS lenguaje
LEFT JOIN users_lenguajes AS usuario_lenguajes
ON lenguaje.lenguaje_id = usuario_lenguajes.lenguaje_id
LEFT JOIN users AS usuario
ON usuario_lenguajes.user_id = usuario.user_id;

--6. El reporte Maestro ( Multiples Uniones)
SELECT usuario.name AS nombre_usuario, usuario.lastname AS apellido_usuario,
        identificacion.dni_number, empresa.name AS nombre_empresa
FROM users AS usuario
INNER JOIN dni AS identificacion
ON usuario.user_id = identificacion.user_id
INNER JOIN companies AS empresa
ON usuario.company_id = empresa.company_id;