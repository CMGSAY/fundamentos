

SELECT sum(precio * stock ) AS inversion_tota
FROM productos;

SELECT company_id, COUNT(user_id)
FROM usuarios
GROUP BY company_id;

SELECT categoria, SUM(stock)
FROM producto
GROUP BY categoria
HAVING SUM(stock) > 100;

SELECT edad, COUNT(*) AS 'Cantidad Usuarios'
FROM usuarios
GROUP BY edad 
HAVING COUNT(*) >2;


SELECT proveedor_id, SUM(stock) AS 'Total stock'
FROM  productos
WHERE proveedor_id >5
GROUP BY proveedor_id

SELECT poveedor_id,  AVG(precio) AS 'Promedio Producto'
FROM productos
WHERE STOCK > 10 
GROUP BY proveedor_id


https://www.scrumstudy.com/certification/scrum-fundamentals-certified