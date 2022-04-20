DELIMITER $$
CREATE PROCEDURE `Search_Crypto_Tickers`(
    IN in_ticker_query CHAR(250)
)
BEGIN
    
    -- create a temporary table to hold the FTS search results
    CREATE TEMPORARY TABLE IF NOT EXISTS Temp_Crypto_Tickers
    SELECT 
        ct.ticker AS ticker,
        ct.name AS name, 
        ct.baseCurrency AS baseCurrency,
        ct.quoteCurrency AS quoteCurrency,
        MATCH(ct.ticker) AGAINST(in_ticker_query IN NATURAL LANGUAGE MODE) AS match_ticker,
        MATCH(ct.name) AGAINST(in_ticker_query IN NATURAL LANGUAGE MODE) AS match_name,
        MATCH(ct.name, ct.ticker) AGAINST(in_ticker_query IN NATURAL LANGUAGE MODE) AS match_combined,
        (SELECT match_ticker + match_name + match_combined) AS match_score
    FROM 
        Crypto_Tickers ct
    GROUP BY 
        ct.ticker;
    
    -- select the matching tickers
    SELECT 
        ct.ticker AS ticker,
        ct.name AS name, 
        ct.baseCurrency AS baseCurrency,
        ct.quoteCurrency AS quoteCurrency
    FROM 
        Temp_Crypto_Tickers ct
    WHERE 
        ct.match_score > 1
    GROUP BY 
        ct.ticker
    ORDER BY 
        match_score DESC;
    
    -- drop the temporary table
    DROP TABLE Temp_Crypto_Tickers;
    
END$$
DELIMITER ;