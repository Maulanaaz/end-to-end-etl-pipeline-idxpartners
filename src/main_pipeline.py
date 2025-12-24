# This code belongs to Maulana Zulfikar Aziz

import pandas as pd
import pyodbc
import warnings

warnings.filterwarnings('ignore')

if __name__=="__main__" :
    try:
        print("Starting ETL Job...")
        raw_account, raw_customer, raw_branch, raw_transaction = extract_data()
        staging(raw_account, raw_customer, raw_branch, raw_transaction)
        clean_account, clean_customer, clean_branch, clean_factsales = transform_data()
        load_dimension(clean_account, clean_customer, clean_branch)
        load_fact(clean_factsales)
        print("ETL job is finished")
        print("")
        print("--- Menu Daily Transaction ---")
        startdate = input("Insert start date (format : YYYY-MM-DD) : ")
        enddate = input("Insert end date (format : YYYY-MM-DD) : ")
        get_daily_transaction(startdate, enddate)
        print("")
        print("--- Menu Balance Per Customer ---")
        name = input("Insert customer name : ")
        get_balance_per_customer(name)
    except Exception as e :
        print(f"Error : {e}")