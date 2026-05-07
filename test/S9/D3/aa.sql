CREATE TABLE `lenguajes` (
  `lenguaje_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`lenguaje_id`)
)

CREATE TABLE `users_lenguajes` (
  `users_lenguajes_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `lenguaje_id` int DEFAULT NULL,
  PRIMARY KEY (`users_lenguajes_id`),
  UNIQUE KEY `user_id` (`user_id`,`lenguaje_id`),
  KEY `lenguaje_id` (`lenguaje_id`),
  CONSTRAINT `users_lenguajes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `users_lenguajes_ibfk_2` FOREIGN KEY (`lenguaje_id`) REFERENCES `lenguajes` (`lenguaje_id`)
)

