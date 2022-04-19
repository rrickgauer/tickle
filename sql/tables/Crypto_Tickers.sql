CREATE TABLE Crypto_Tickers(
    ticker CHAR(50) NOT NULL UNIQUE,
    name CHAR(100),
    baseCurrency CHAR(30),
    quoteCurrency CHAR(30),
    PRIMARY KEY (ticker),
    FULLTEXT(ticker, name),
    INDEX crypto_tickers_index_name (name)
);