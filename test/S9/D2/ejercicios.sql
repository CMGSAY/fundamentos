SELECT lenguajes.name, users.name
FROM users_lenguajes
RIGHT JOIN lenguajes
ON users_lenguajes.lenguaje_id = lenguajes.lenguaje_id
RIGHT JOIN users
ON users_lenguajes.user_id = users.user_id

https://www.youtube.com/watch?v=AHyCBSumqIM&list=PLrn7pb9emo5WAfg389e3NB6hR3YuQlhM3