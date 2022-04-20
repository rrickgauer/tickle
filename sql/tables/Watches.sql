CREATE TABLE `Watches` (
  `id` CHAR(36) NOT NULL,
  `ticker_type` INT UNSIGNED NOT NULL,
  `ticker` CHAR(20) NOT NULL,
  `price` DECIMAL(10,2) DEFAULT NULL,
  `watch_type` INT UNSIGNED NOT NULL,
  `email` VARCHAR(320) DEFAULT NULL,
  `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `closed_on` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `Watches_Watch_Type_Fk_idx` (`ticker_type`),
  KEY `Watches_Watch_Type_FK` (`watch_type`),
  CONSTRAINT `Watches_Ticker_Type_FK` FOREIGN KEY (`ticker_type`) REFERENCES `Ticker_Types` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `Watches_Watch_Type_FK` FOREIGN KEY (`watch_type`) REFERENCES `Watch_Types` (`id`) ON UPDATE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;
