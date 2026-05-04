-- ifnull
-- es una funcion que me va a permitir reemplazar 
SELECT name, lastname, ifnull(age, 0) AS age
FROM users;