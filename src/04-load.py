def load_dimension(clean_account, clean_customer, clean_branch) :
    print("Starting dimension load process ...")
    jobs = ((clean_customer, "DimCustomer",clean_customer.columns.tolist(), ["?" for i in range(len(clean_customer.columns))]),
            (clean_account, "DimAccount", clean_account.columns.tolist(), ["?" for i in range(len(clean_account.columns))]),
            (clean_branch, "DimBranch",clean_branch.columns.tolist(), ["?" for i in range(len(clean_branch.columns))]))
    with pyodbc.connect(dw_conn) as conn :
        cursor = conn.cursor()
        for job in jobs :
            df_clean = job[0].copy()
            id_col = df_clean.columns[0]
            existing_data = pd.read_sql(f"SELECT {id_col} FROM {job[1]}",conn)
            new_data = df_clean[~df_clean[id_col].isin(existing_data[id_col])]
            if not new_data.empty :
                cols = ",".join(job[2])
                values = ",".join(job[3])
                query = f"INSERT INTO {job[1]} ({cols}) VALUES ({values})"
                data = new_data.values.tolist()
                cursor.executemany(query,data)
                cursor.commit()
    print("Dimension load process is finished.")

def load_fact(clean_transaction) :
    print("Starting fact load process ...")
    with pyodbc.connect(dw_conn) as conn :
        cursor = conn.cursor()
        existing_data = pd.read_sql("SELECT TransactionID FROM FactTransaction",conn)
        new_data = clean_transaction[~clean_transaction["TransactionID"].isin(existing_data["TransactionID"])]
        if not new_data.empty :
            query = """
            INSERT INTO FactTransaction (TransactionID, AccountID, TransactionDate, Amount, TransactionType, BranchID) VALUES (?, ?, ?, ?, ?, ?)
            """
            data = new_data.values.tolist()
            cursor.executemany(query,data)
            cursor.commit()
    print("Load fact process is finished.")