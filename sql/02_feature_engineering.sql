CREATE VIEW fraud_features AS
SELECT 
    *,
    (CAST(oldbalanceOrg AS FLOAT) - CAST(amount AS FLOAT)) - CAST(newbalanceOrig AS FLOAT) AS errorBalanceOrig,
    (CAST(oldbalanceDest AS FLOAT) + CAST(amount AS FLOAT)) - CAST(newbalanceDest AS FLOAT) AS errorBalanceDest
FROM dbo.transactions
WHERE TYPE IN ('TRANSFER', 'CASH_OUT')