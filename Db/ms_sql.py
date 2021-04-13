import os
import pyodbc 

## pip install pyodbc
## brew install unixodbc
## brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
## brew install msodbcsql17 mssql-tools


SQL_SERVER="localhost,1433"
SQL_SERVER="127.0.0.1,1433"
DB="eBuilderCore"
USER="sa"
PASSWORD=os.environ["PASSWORD"]
TABLE="UalEvents"

SQL__CONNECTIONSTRING=f"SERVER={SQL_SERVER};DATABASE={DB};"'Trusted_Connection=yes;'
SQL__CONNECTIONSTRING=f"SERVER={SQL_SERVER};DATABASE={DB};UID={USER};PWD={PASSWORD};"

print(pyodbc.drivers())

DRIVER = "{ODBC Driver 17 for SQL Server}"
CONN_STR = f'DRIVER={DRIVER};{SQL__CONNECTIONSTRING}'
print(f"Connecting to SQL with {CONN_STR}")
conn = pyodbc.connect(CONN_STR)
print("Connected")

SQL = f"SELECT * FROM {TABLE}"
cursor = conn.cursor()
cursor.execute(SQL)
for row in cursor:
    print(row)

INSERT = "insert into UalEvents values (123, '{headers:null, topic: \"test-audit\", key: null, message: \"rlv_0001\"}')"

cursor.execute(INSERT)
cursor.commit()

cursor.execute(SQL)
for row in cursor:
    print(row)

conn.close()
