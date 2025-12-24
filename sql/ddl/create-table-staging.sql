USE DWH;
GO


CREATE TABLE StgCustomer(
CustomerID INT,
CustomerName VARCHAR(50),
Address VARCHAR(100),
CityName VARCHAR(20),
StateName VARCHAR(20),
Age INT,
Gender VARCHAR(10),
Email VARCHAR(50),
LoadedDate DATETIME DEFAULT GETDATE()
);
GO
CREATE TABLE StgAccount(
AccountID INT,
CustomerID INT, 
AccountType VARCHAR(20),
Balance INT,
DateOpened VARCHAR(100),
Status VARCHAR(20),
LoadedDate DATETIME DEFAULT GETDATE()
);
GO
CREATE TABLE StgBranch(
BranchID INT,
BranchName VARCHAR(20),
BranchLocation VARCHAR(100),
LoadedDate DATETIME DEFAULT GETDATE()
);
GO

CREATE TABLE StgFactTransaction(
TransactionID INT,
AccountID INT,
TransactionDate VARCHAR(100),
Amount INT,
TransactionType VARCHAR(20),
BranchID INT,
LoadedDate DATETIME DEFAULT GETDATE()
);
GO