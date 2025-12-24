# This code belongs to Maulana Zulfikar Aziz

import pandas as pd
import pyodbc
import warnings

warnings.filterwarnings('ignore')

SERVER = "***"
DRIVER = "ODBC Driver 17 for SQL Server"

source_conn = f'SERVER={SERVER};DRIVER={DRIVER};DATABASE=sample;Trusted_Connection=yes'
dw_conn = f'SERVER={SERVER};DRIVER={DRIVER};DATABASE=DWH;Trusted_Connection=yes'
def extract_data() :
    # Extract from SQL SERVER
    print("Extracting data from various sources ...")
    list_query = {
        "DimAccount":"""
        SELECT account_id AS AccountID, customer_id AS CustomerID, account_type AS AccountType, balance AS Balance, 
        date_opened AS DateOpened, status AS Status FROM account
        """,
        "DimCustomer": """
        SELECT cu.customer_id AS CustomerID, cu.customer_name AS CustomerName, cu.address AS Address, ci.city_name AS CityName, 
        s.state_name AS StateName, cu.age AS Age, cu.gender AS Gender, cu.email AS Email
        FROM customer as cu
        LEFT JOIN city AS ci ON cu.city_id=ci.city_id
        LEFT JOIN state AS s ON ci.state_id=s.state_id
        """,
        "DimBranch" : "SELECT branch_id AS BranchID, branch_name AS BranchName, branch_location AS BranchLocation FROM branch",
        "Transaction" : "SELECT transaction_id, account_id, transaction_date, amount, transaction_type, branch_id FROM transaction_db"
    }
    df = {}
    with pyodbc.connect(source_conn) as conn :
        for nama_tabel, query in list_query.items() :
            df[nama_tabel] = pd.read_sql(query, conn)
    transaction_sql = pd.DataFrame(df["Transaction"])
    transaction_csv = pd.read_csv("transaction_csv.csv")
    transaction_excel = pd.read_excel("transaction_excel.xlsx")
    raw_transaction = pd.concat([transaction_sql, transaction_csv, transaction_excel], ignore_index=True)
    change_columns = {"transaction_id":"TransactionID", "account_id":"AccountID", "transaction_date":"TransactionDate", "amount":"Amount",
                      "transaction_type":"TransactionType", "branch_id":"BranchID"}
    raw_transaction.rename(columns=change_columns, inplace=True)
    raw_account = pd.DataFrame(df["DimAccount"])
    raw_customer = pd.DataFrame(df["DimCustomer"])
    raw_branch = pd.DataFrame(df["DimBranch"])
    
    print("Extraction job is finished.")
    return raw_account, raw_customer, raw_branch, raw_transaction