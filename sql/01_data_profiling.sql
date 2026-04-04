-- 1. Row count 

SELECT COUNT (*) as total_rows
FROM dbo.transactions;

-- 2. Data preview

SELECT TOP 5 * 
FROM dbo.transactions;

-- 3. Schema

SELECT
COLUMN_NAME,
DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME= 'transactions';

-- 4. Target variable distribution (class imbalance)
SELECT 
    isFraud,
    COUNT (*) AS count
FROM dbo.transactions
GROUP BY isFraud;