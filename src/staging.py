def staging(raw_account, raw_customer, raw_branch, raw_transaction) :
    print("Staging is in process ...")
    jobs = ((raw_account, "StgAccount", raw_account.columns.tolist(), ["?" for i in range(len(raw_account.columns))]),
          (raw_customer, "StgCustomer",raw_customer.columns.tolist(), ["?" for i in range(len(raw_customer.columns))]),
          (raw_branch, "StgBranch",raw_branch.columns.tolist(), ["?" for i in range(len(raw_branch.columns))]),
          (raw_transaction, "StgFactTransaction", raw_transaction.columns.tolist(), ["?" for i in range(len(raw_transaction.columns))]))
    with pyodbc.connect(dw_conn) as conn :
        cursor = conn.cursor()
        for job in jobs :
            cols = ",".join(job[2])
            values = ",".join(job[3])
            query = f"INSERT INTO {job[1]} ({cols}) VALUES ({values})"
            cursor.execute(f"TRUNCATE TABLE {job[1]}") 
            data = job[0].values.tolist()
            cursor.executemany(query,data)
            cursor.commit()
    print("Staging process is finished.")