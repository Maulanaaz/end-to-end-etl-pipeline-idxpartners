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