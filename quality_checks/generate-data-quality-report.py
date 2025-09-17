import os, psycopg2
import pandas as pd
from tabulate import tabulate
import mytests
from dataqualitychecks import run_data_quality_check
from dotenv import load_dotenv

from dbconnect import pgpassword

load_dotenv()

pguser = os.getenv("PGUSER")
pgpassword = os.getenv("PGPASSWORD")
pgdatabase = os.getenv("PGDATABASE")

# Connect to database
conn = psycopg2.connect(
		user=pguser,
	    password=pgpassword,
	    host="localhost",
	    port="5432",
	    database=pgdatabase
)
print("Connected to data warehouse")

# Start of data quality checks
results = []
tests = {key: value for key, value in mytests.__dict__.items() if key.startswith('test')}
for testname, test in tests.items():
    test["conn"] = conn
    results.append(run_data_quality_check(**test))

# Print(results)
df = pd.DataFrame(results, columns=['Test Name', 'Table', 'Column', 'Test Passed'])
df.index += 1
print(tabulate(df, headers="keys", tablefmt="psql"))

# End of data quality checks
conn.close()
print("Disconnected from data warehouse")