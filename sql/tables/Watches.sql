CREATE TABLE Watches
(
    id CHAR(36) NOT NULL UNIQUE,
    ticker CHAR(20) NOT NULL,
    price DECIMAL(10, 2),
    watch_type INT UNSIGNED NOT NULL,
    email VARCHAR(320),
    created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    closed_on TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (watch_type) REFERENCES Watch_Types(id) ON UPDATE CASCADE
);