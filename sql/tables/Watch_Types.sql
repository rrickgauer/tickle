CREATE TABLE Watch_Types
(
    id INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    name CHAR(50) NOT NULL,
    description CHAR(250),
    created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);