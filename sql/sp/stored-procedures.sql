USE DWH;
GO

CREATE OR ALTER PROCEDURE DailyTransaction
	@StartDate DATE,
	@EndDate DATE
AS
BEGIN
	SELECT TransactionDate, COUNT(1) AS TotalTransaction, SUM(Amount) AS TotalAmount
	FROM FactTransaction
	WHERE TransactionDate Between @StartDate AND @EndDate
	GROUP BY TransactionDate;
END;
GO

EXEC DailyTransaction @StartDate='2024-01-18', @EndDate='2024-01-20';
GO

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
