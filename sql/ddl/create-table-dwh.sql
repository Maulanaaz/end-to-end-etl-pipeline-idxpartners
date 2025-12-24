CREATE DATABASE DWH;
GO

USE DWH;
GO


CREATE TABLE DimCustomer(
CustomerID INT PRIMARY KEY NOT NULL,
CustomerName VARCHAR(50),
Address VARCHAR(100),
CityName VARCHAR(20),
StateName VARCHAR(20),
Age INT,
Gender VARCHAR(10),
Email VARCHAR(50)
);
GO
CREATE TABLE DimAccount(
AccountID INT PRIMARY KEY NOT NULL,
CustomerID INT FOREIGN KEY REFERENCES DimCustomer(CustomerID), 
AccountType VARCHAR(20),
Balance INT,
DateOpened DATE,
Status VARCHAR(20)
);
GO
CREATE TABLE DimBranch(
BranchID INT PRIMARY KEY NOT NULL,
BranchName VARCHAR(20),
BranchLocation VARCHAR(100)
);
GO

CREATE TABLE FactTransaction(
TransactionID INT PRIMARY KEY NOT NULL,
AccountID INT FOREIGN KEY REFERENCES DimAccount(AccountID),
TransactionDate DATE,
Amount INT,
TransactionType VARCHAR(20),
BranchID INT FOREIGN KEY REFERENCES DimBranch(BranchID)
);
GO