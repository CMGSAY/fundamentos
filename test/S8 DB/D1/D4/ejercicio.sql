-- Creación de la tabla de inventario
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10, 2),
    stock INT,
    fecha_ingreso DATE,
    proveedor_id INT
);

-- Inserción de datos de prueba
INSERT INTO productos (nombre, categoria, precio, stock, fecha_ingreso, proveedor_id) VALUES
('Laptop Pro', 'Electrónica', 1200.00, 15, '2024-01-10', 1),
('Mouse Inalámbrico', 'Electrónica', 25.50, 100, '2024-02-15', 2),
('Monitor 4K', 'Electrónica', 450.00, 8, '2023-11-20', 1),
('Silla Ergonómica', 'Mobiliario', 250.00, 20, '2024-03-01', 3),
('Escritorio Gamer', 'Mobiliario', 350.00, 5, '2023-12-15', 3),
('Teclado Mecánico', 'Electrónica', 85.00, NULL, '2024-04-10', 2),
('Audífonos Noise Cancelling', 'Electrónica', 150.00, 30, '2024-01-05', 2),
('Lámpara LED', 'Hogar', 45.00, 50, '2024-03-20', NULL),
('Cámara Web HD', 'Electrónica', 60.00, 0, '2024-02-10', 1),
('Cafetera Italiana', 'Hogar', 35.00, 12, '2024-04-01', NULL);