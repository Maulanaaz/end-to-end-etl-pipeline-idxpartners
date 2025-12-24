CREATE OR ALTER PROCEDURE BalancePerCustomer
@name VARCHAR(50)
AS
BEGIN
	SELECT 
		c.CustomerName, 
		a.AccountType, 
		a.Balance,
		a.Balance + COALESCE(SUM(CASE
			WHEN t.TransactionType='Deposit' THEN t.Amount
			ELSE -t.Amount
		END),0) AS CurrentBalance
	FROM FactTransaction AS t
	LEFT JOIN DimAccount AS a ON t.AccountID=a.AccountID
	LEFT JOIN DimCustomer AS c ON a.CustomerID = c.CustomerID
	WHERE c.CustomerName LIKE '%'+UPPER(@name)+'%' AND a.Status='active'
	GROUP BY c.CustomerName, a.AccountType, a.Balance;
END;
GO

EXEC BalancePerCustomer
@name = 'Shelly';
GO