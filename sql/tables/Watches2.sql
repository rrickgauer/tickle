-- CREATE TABLE Watches2
-- (
--     id CHAR(36) NOT NULL UNIQUE,
--     pair_type INT UNSIGNED NOT NULL,
--     pair_id INT UNSIGNED NOT NULL,
--     price DECIMAL(10,2) NOT NULL,
--     watch_type INT UNSIGNED NOT NULL,
--     email VARCHAR(320) NOT NULL,
--     created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     closed_on TIMESTAMP,
--     PRIMARY KEY (id),
--     FOREIGN KEY (pair_type) REFERENCES Pair_Types(id) ON UPDATE CASCADE,
--     FOREIGN KEY (watch_type) REFERENCES Watch_Types (id) ON UPDATE CASCADE
-- );


CREATE TABLE Watches2 (
    id CHAR(36) NOT NULL UNIQUE,
    watch_type INT UNSIGNED NOT NULL,
    tag CHAR(250) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    email VARCHAR(320) NOT NULL,
    created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    closed_on TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (watch_type) REFERENCES Watch_Types (id) ON UPDATE CASCADE
);