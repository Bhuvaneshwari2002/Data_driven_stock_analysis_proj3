CREATE DATABASE stock_analysis;
USE stock_analysis;

CREATE TABLE stocks (
  ticker VARCHAR(32) PRIMARY KEY,
  company VARCHAR(255),
  sector VARCHAR(128)
);

CREATE TABLE prices (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  ticker VARCHAR(35) NOT NULL,
  date DATETIME NOT NULL,
  open DOUBLE,
  high DOUBLE,
  low DOUBLE,
  close DOUBLE,
  volume BIGINT,
  daily_return DOUBLE,
  UNIQUE KEY uq_ticker_date (ticker, date)
);

CREATE INDEX idx_prices_ticker_date ON prices(ticker, date);
CREATE INDEX idx_prices_date ON prices(date);

select * from prices;
select * from stocks;
