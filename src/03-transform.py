def transform_data():
    print("Reading data from stage ...")
    with pyodbc.connect(dw_conn) as conn :
        print("Transforming the data...")
        raw_account = pd.read_sql("SELECT AccountID, CustomerID, AccountType, Balance, DateOpened, Status FROM StgAccount", conn)
        raw_customer = pd.read_sql("SELECT CustomerID, CustomerName, Address, CityName, StateName, Age, Gender, Email FROM StgCustomer", conn)
        raw_branch = pd.read_sql("SELECT BranchID, BranchName, BranchLocation FROM StgBranch", conn)
        raw_transaction = pd.read_sql("SELECT TransactionID, AccountID, TransactionDate, Amount, TransactionType, BranchID FROM StgFactTransaction", 
                                      conn)

        # TRANSFORM : ACCOUNT
        clean_account = raw_account.drop_duplicates(subset=["AccountID"],keep="first")
        clean_account["DateOpened"] = pd.to_datetime(clean_account["DateOpened"],dayfirst=False, format="mixed").dt.strftime('%Y-%m-%d')

        # TRANSFORM : CUSTOMER
        clean_customer = raw_customer.drop_duplicates(subset=["CustomerID"],keep="first")
        cols_upper = ["CustomerName", "Address", "CityName", "StateName", "Gender"]
        clean_customer[cols_upper] = clean_customer[cols_upper].apply(lambda x : x.str.upper())

        # TRANSFORM : BRANCH
        clean_branch = raw_branch.drop_duplicates(subset=["BranchID"],keep="first")

        # TRANSFORM : TRANSACTION
        clean_transaction = raw_transaction.drop_duplicates(subset=["TransactionID"], keep="first")
        clean_transaction["TransactionDate"] = pd.to_datetime(clean_transaction["TransactionDate"], dayfirst=False, 
                                                              format="mixed").dt.strftime('%Y-%m-%d')

        print("Transformation process finished.")
        return clean_account, clean_customer, clean_branch, clean_transaction