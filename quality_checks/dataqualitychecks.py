from time import time, ctime

conn = None
def run_data_quality_check(**options):
    print("*" * 50)
    print(ctime(time()))
    start_time = time()
    testname = options.pop("testname")
    test = options.pop("test")
    print(f"Starting test {testname}")
    status = test(**options)
    print(f"Finished test {testname}")
    print(f"Test Passed {status}")
    end_time = time()
    options.pop("conn")
    print("Test Parameters")
    for key, value in options.items():
        print(f"{key} = {value}")
    print()
    print("Duration : ", str(end_time - start_time))
    print(ctime(time()))
    print("*" * 50)
    return testname,options.get('table'),options.get('column'),status

# Check for nulls
def check_for_nulls(column, table, conn=conn):
    sql = f'SELECT COUNT(*) FROM "{table}" WHERE {column} IS NULL'
    cursor = conn.cursor()
    cursor.execute(sql)
    row_count = cursor.fetchone()
    cursor.close()
    return bool(row_count)

# Check for min max range
def check_for_min_max(table, column, minimum, maximum, conn=conn):
    sql = f'SELECT COUNT(*) FROM "{table}" WHERE  {column} < {minimum} OR {column} > {maximum}'
    cursor = conn.cursor()
    cursor.execute(sql)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count[0])

# Check for any invalid entries
def check_for_valid_values(table, column, valid_values, conn=conn):
    sql = f'SELECT DISTINCT({column}) FROM "{table}"'
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)
    actual_values = {x[0] for x in result}
    print(actual_values)
    status = [value in valid_values for value in actual_values]
    #print(status)
    cursor.close()
    return all(status)

# Check for duplicate entries
def check_for_duplicates(table, column, conn=conn):
    sql = f'SELECT COUNT({column}) FROM "{table}" GROUP BY {column} HAVING COUNT({column}) > 1'
    cursor = conn.cursor()
    cursor.execute(sql)
    row_count = cursor.fetchone()
    #print(row_count)
    cursor.close()
    return not bool(row_count)