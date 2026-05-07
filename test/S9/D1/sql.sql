SELECT *,
CASE 
	WHEN AGE <18 THEN 'menor edad'
    WHEN age =18 THEN 'acaba de cumplir la mayoria de edad'
    ELSE 'Mayor de edad'
END AS 'Es mayor de edad'
FROM users;

