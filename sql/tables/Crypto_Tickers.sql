CREATE TABLE `Crypto_Tickers` (
  `ticker` CHAR(50) NOT NULL,
  `name` CHAR(100) DEFAULT NULL,
  `baseCurrency` CHAR(30) DEFAULT NULL,
  `quoteCurrency` CHAR(30) DEFAULT NULL,
  PRIMARY KEY (`ticker`),
  UNIQUE KEY `ticker` (`ticker`),
  KEY `index_name` (`name`),
  FULLTEXT KEY `index_ticker_name_fts` (`name`,`ticker`),
  FULLTEXT KEY `index_name_fts` (`name`),
  FULLTEXT KEY `index_ticker_fts` (`ticker`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8MB4 COLLATE=UTF8MB4_0900_AI_CI;