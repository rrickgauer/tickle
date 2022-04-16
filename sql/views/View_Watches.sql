CREATE VIEW View_Watches AS 
SELECT
    w.id AS id,
    UPPER(w.ticker) AS ticker,
    w.price AS price,
    w.watch_type AS watch_type,
    w.email AS email,
    w.created_on AS created_on,
    w.closed_on AS closed_on
FROM 
    Watches w;