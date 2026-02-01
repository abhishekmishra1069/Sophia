-- db-init/init.sql
CREATE TABLE IF NOT EXISTS stock_prices (
    symbol TEXT PRIMARY KEY,
    price NUMERIC,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);