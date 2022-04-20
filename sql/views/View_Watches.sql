CREATE VIEW View_Watches AS
SELECT 
    w.id AS id,
    w.ticker AS ticker,
    w.ticker_type AS ticker_type,
    tt.name AS ticker_name,
    w.price AS price,
    w.watch_type AS watch_type,
    wt.name AS watch_type_name,
    w.email AS email,
    w.created_on AS created_on,
    w.closed_on AS closed_on
FROM
    Watches w
    LEFT JOIN Ticker_Types tt ON tt.id = w.ticker_type
    LEFT JOIN Watch_Types wt ON wt.id = w.watch_type;