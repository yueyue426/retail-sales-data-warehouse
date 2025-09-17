import psycopg2
pgpassword = 1234
conn = None
try:
    conn = psycopg2.connect(
        user="Chloe",           # role name
        password=pgpassword,    # the password you set
        host="localhost",       # local machine, not "postgres"
        port="5432",            # default PostgreSQL port
        database="stagingDW"    # your project database
    )
except Exception as e:
    print("Error connecting to data warehouse")
    print(e)
else:
    print("Successfully connected to warehouse")
finally:
    if conn:
        conn.close()
        print("Connection closed")
