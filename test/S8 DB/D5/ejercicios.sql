-- 1. SELECT (El Observador)
-- Básico: Selecciona todos los nombres de los productos.
SELECT nombre
FROM productos;
-- Intermedio: Selecciona el nombre, el precio y el stock de la tabla.
SELECT nombre,precio, stock
FROM productos;
-- Retador: Selecciona todas las columnas disponibles en la tabla de productos.
SELECT *
FROM productos;


-- 2. DISTINCT (El Filtro de Unicidad)
-- Básico: Obtén una lista de las categorías sin que se repitan.
SELECT DISTINCT(categoria)
FROM productos;
-- Intermedio: Obtén una lista única de los proveedor_id que tienen productos.
SELECT DISTINCT(proveedor_id)
FROM productos;
-- Retador: Muestra los diferentes precios que existen actualmente en el inventario.
SELECT DISTINCT(precio)
FROM productos;


-- 3. WHERE (El Guardián)
-- Básico: Selecciona los productos que pertenecen a la categoría 'Hogar'.
SELECT *
FROM productos
WHERE categoria = 'Hogar';
-- Intermedio: Selecciona los productos cuyo precio sea exactamente 1200.00.
SELECT *
FROM productos
WHERE precio = 1200.00
-- Retador: Selecciona nombres de productos de 'Electrónica' con un stock menor a 10.
SELECT nombre, stock, categoria
FROM productos
WHERE categoria = 'Electronica' AND stock < 10;


-- 4. ORDER BY (El Organizador)
-- Básico: Lista los productos ordenados por nombre alfabéticamente.
SELECT nombre
FROM productos
ORDER BY nombre asc;
-- Intermedio: Ordena los productos por precio de mayor a menor.
SELECT nombre, precio
FROM productos
ORDER BY precio desc;
-- Retador: Ordena por categoría y, dentro de cada categoría, por stock descendente.
SELECT categoria, nombre, precio
FROM productos
ORDER BY categoria, stock desc;


-- 5. LIKE (El Detective de Patrones)
-- Básico: Busca productos que empiecen con la palabra 'Monitor'.
SELECT categoria, nombre, precio
FROM productos
WHERE nombre LIKE 'Monitor%';
-- Intermedio: Busca productos que terminen con la letra 'o'.
SELECT categoria, nombre, precio
FROM productos
WHERE nombre LIKE '%o';
-- Retador: Busca productos que tengan la palabra 'Inalámbrico' en cualquier parte del nombre, ordenados por precio.
SELECT categoria, nombre, precio
FROM productos
WHERE nombre LIKE '%Inalámbrico%';


-- 6. AND / OR / NOT (Los Operadores Lógicos)
-- Básico: Productos de 'Electrónica' Y que cuesten menos de $100.
SELECT nombre, stock, categoria
FROM productos
WHERE categoria = 'Electronica' AND precio < 100;
-- Intermedio: Productos que sean 'Hogar' O 'Mobiliario'.
SELECT categoria, nombre, precio
FROM productos
WHERE categoria = 'Hogar' OR categoria = 'Mobiliario';
-- Retador: Productos que NO sean 'Electrónica' y tengan stock mayor a 0, ordenados por categoría.
SELECT categoria, nombre, precio, stock
FROM productos
WHERE categoria != 'Electrónica' AND stock > 0 
ORDER BY categoria;

-- 7. LIMIT (El Recortador)
-- Básico: Muestra los primeros 2 productos de la tabla.
SELECT id, categoria, nombre, precio, stock
FROM productos
LIMIT 2;
-- Intermedio: Muestra los 5 productos más caros (usa ORDER BY y LIMIT).
SELECT id, categoria, nombre, precio, stock
FROM productos
ORDER BY precio desc
LIMIT 5;
-- Retador: Selecciona el nombre del producto con menos stock (solo 1 resultado).
SELECT id, categoria, nombre, precio, stock
FROM productos
ORDER BY stock asc
LIMIT 1;


-- 8. NULL (El Buscador de Vacíos)
-- Básico: Selecciona productos que no tengan proveedor_id asignado.
SELECT id, categoria, nombre, precio, stock, proveedor_id
FROM productos
WHERE proveedor_id IS NOT NULL;
-- Intermedio: Selecciona productos donde el stock sea nulo.
SELECT id, categoria, nombre, precio, stock, proveedor_id
FROM productos
WHERE stock IS NOT NULL;
-- Retador: Selecciona productos con proveedor asignado pero que NO tengan stock definido.

SELECT id, categoria, nombre, precio, stock, proveedor_id
FROM productos
WHERE proveedor_id IS NOT NULL
AND stock IS NULL;

-- 9. MIN / MAX (Los Extremos)
-- Básico: Encuentra el precio más bajo de toda la tabla.
SELECT MIN(precio)
FROM productos;
-- Intermedio: Encuentra el precio más alto de la categoría 'Mobiliario'.
SELECT MAX(precio)
FROM productos
WHERE categoria = 'Mobiliario';
-- Retador: Selecciona el stock máximo entre los productos que cuestan menos de $500.
SELECT MAX(stock)
FROM productos
WHERE precio <500;

-- 10. COUNT (El Contador)
-- Básico: Cuenta cuántos registros totales tiene la tabla.
SELECT COUNT(nombre)
FROM productos;
-- Intermedio: Cuenta cuántos productos tienen un proveedor asignado.
SELECT COUNT(nombre)
FROM productos
WHERE proveedor_id IS NOT NULL;
-- Retador: Cuenta cuántos productos de 'Electrónica' tienen un precio mayor a $100
SELECT COUNT(nombre)
FROM productos
WHERE categoria = 'Electrónica' AND precio > 100;


-- 11. SUM (El Acumulador)
-- Básico: Suma todo el stock disponible en la tienda.
SELECT SUM(stock)
FROM productos;
-- Intermedio: Suma el precio de todos los productos de la categoría 'Mobiliario'.
SELECT SUM(stock)
FROM productos
WHERE categoria = 'Mobiliario';
-- Retador: Calcula el valor total monetario del stock (precio * stock) para todos los productos.


-- 12. AVG (El Promediador)
-- Básico: Calcula el precio promedio de todos los productos.
SELECT AVG( precio) AS Promedio
FROM productos;
-- Intermedio: Calcula el promedio de stock de los productos de 'Electrónica'.
SELECT AVG(stock) AS Promedio
FROM productos
WHERE categoria = 'Electrónica';
-- Retador: Obtén el promedio de precio de los productos que entraron en el año 2024.
SELECT AVG(precio) AS Promedio
FROM productos
WHERE fecha_ingreso LIKE '2024%';


-- 13. IN (El Selector de Listas)
-- Básico: Selecciona productos cuyo id sea 1, 3 o 5.
SELECT id, nombre, precio
FROM productos
WHERE id IN (1, 3, 5);
-- Intermedio: Selecciona productos cuyas categorías sean 'Hogar' o 'Electrónica' usando IN.
SELECT id, nombre, precio, categoria
FROM productos
WHERE categoria IN ('Hogar', 'Electrónica');
-- Retador: Selecciona productos de los proveedores 1 y 2, ordenados por nombre.
SELECT id, nombre, precio, proveedor_id
FROM productos
WHERE proveedor_id IN (1,2) ORDER BY  nombre;


-- 14. BETWEEN (El Definidor de Rangos)
-- Básico: Selecciona productos con precio entre $50 y $300.
SELECT id, nombre, precio, proveedor_id
FROM productos
WHERE precio BETWEEN 50 and 300;
-- Intermedio: Selecciona productos que ingresaron entre '2024-01-01' y '2024-03-31'
SELECT id, nombre, precio, fecha_ingreso
FROM productos
WHERE fecha_ingreso BETWEEN '2024-01-01' and '2024-03-31';
-- Retador: Selecciona productos con stock entre 5 y 20, que pertenezcan a 'Mobiliario'
SELECT id, nombre, precio, stock, categoria
FROM productos
WHERE categoria = 'Mobiliario' AND stock BETWEEN 5 and 20;


-- 15. ALIAS (El Apodador)
-- Básico: Selecciona el nombre del producto y llámalo "Articulo".
SELECT nombre AS Articulo
FROM productos;
-- Intermedio: Selecciona el precio y llámalo "Costo_Unitario", ordenado por este nuevo nombre.
SELECT precio AS Costo_Uitario
FROM productos
ORDER BY precio ASC;
-- Retador: Calcula el IVA (precio * 0.13) y muéstralo como "Impuesto_Ventas" para cada producto.
SELECT (precio * 0.13) AS Impuesto_Ventas
FROM productos
ORDER BY precio ASC;


-- 16. CONCAT (El Unionista)
-- Básico: Une el nombre y la categoría en una sola columna.
SELECT CONCAT(nombre, '  ', categoria) AS Nombre_y_Categoria
FROM productos;
-- Intermedio: Crea un mensaje tipo: "El producto [nombre] cuesta [precio]".
SELECT CONCAT('El Producto: ', nombre, ' cuesta: ', precio) AS Producto_Precio
FROM productos;
-- Retador: Crea un código de inventario uniendo el id y las primeras letras de la categoría.
SELECT CONCAT(id, LEFT(categoria, 3)) AS codigo_inventario
FROM productos;


-- 17. GROUP BY (El Agrupador)
-- Básico: Agrupa por categoría para ver cuáles existen.
SELECT categoria
FROM productos
GROUP BY categoria;
-- Intermedio: Muestra la cantidad de productos por cada categoría.
SELECT categoria, COUNT(*) AS cantidad_productos
FROM productos
GROUP BY categoria;
-- Retador: Muestra el precio máximo y mínimo por cada proveedor, ordenado por el precio máximo.
SELECT proveedor_id,MIN(precio) AS precio_minimo, MAX(precio) AS precio_maximo
FROM productos
GROUP BY proveedor_id
ORDER BY proveedor_id;

-- 18. HAVING (El Filtro de Grupos)
-- Básico: Muestra categorías que tengan más de 2 productos.
SELECT categoria, COUNT(*) AS cantidad_productos
FROM productos
GROUP BY categoria
HAVING COUNT(*) > 2;
-- Intermedio: Muestra categorías cuyo precio promedio sea mayor a $200.
SELECT categoria, AVG(precio) AS precio_promedio
FROM productos
GROUP BY categoria
HAVING AVG(precio) > 200;
-- Retador: Muestra los proveedores que tienen más de un producto en stock,
-- filtrando aquellos que sumen un valor total mayor a $500.
SELECT proveedor_id, COUNT(*) AS productos_en_stock, SUM(precio * stock) AS valor_total
FROM productos
WHERE stock > 0
GROUP BY proveedor_id
HAVING COUNT(*) > 1 AND SUM(precio * stock) > 500;
