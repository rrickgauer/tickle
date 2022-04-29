CREATE TABLE `Watches` (
  `id` CHAR(36) NOT NULL,
  `watch_type` INT UNSIGNED NOT NULL,
  `tag` CHAR(250) NOT NULL,
  `symbol` CHAR(50) DEFAULT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `email` VARCHAR(320) NOT NULL,
  `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `closed_on` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `watch_type` (`watch_type`),
  CONSTRAINT `Watches2_ibfk_1` FOREIGN KEY (`watch_type`) REFERENCES `Watch_Types` (`id`) ON UPDATE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;
