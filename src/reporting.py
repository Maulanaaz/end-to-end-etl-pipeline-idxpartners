def get_daily_transaction(start_date, end_date) :
    print(f"\n--- Transaction from {start_date} to {end_date} ---")
    print("\n")
    with pyodbc.connect(dw_conn) as conn :
        cursor = conn.cursor()
        query = "{CALL DailyTransaction (?, ?)}"
        params = (start_date, end_date)
        cursor.execute(query, params)
        rows = cursor.fetchall()
        if rows :
            columns = [column[0] for column in cursor.description]
            df = pd.DataFrame.from_records(rows,columns=columns)
            print(df)
        else :
            print("There is no data that can be shown.")

def get_balance_per_customer(name) :
    print(f"\n--- Balance Information for Customer Named {name} ---")
    print("\n")
    with pyodbc.connect(dw_conn) as conn :
        cursor = conn.cursor()
        query = "{CALL BalancePerCustomer (?)}"
        params = (name)
        cursor.execute(query, params)
        rows = cursor.fetchall()
        if rows :
            columns = [column[0] for column in cursor.description]
            df = pd.DataFrame.from_records(rows,columns=columns)
            print(df)
        else :
            print("There is no data that can be shown.")