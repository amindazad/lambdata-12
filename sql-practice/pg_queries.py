import psycopg2
import os
from dotenv import dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="oops")
DB_USER = os.getenv("DB_USER", default="oops")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="oops")
DB_HOST = os.getenv("DB_HOST", default="oops")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname= DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(conn)

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cur.fetchone()

print(result)