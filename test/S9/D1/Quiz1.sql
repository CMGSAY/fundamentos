-- Ejercicio 1: El Analista de Optimización

SELECT nombre, proyecto AS Nombre_del_Proyecto
FROM empleados_proyectos
WHERE salario > 3800 AND proyecto IS NOT NULL
ORDER BY salario DESC;

--Ejercicio 2: El Auditor de Productividad

SELECT departamento, AVG(horas_semanales)
FROM empleados
GROUP BY departamento
HAVING AVG(horas_semanales) > 30