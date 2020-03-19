import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="oops")
DB_USER = os.getenv("DB_USER", default="oops")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="oops")
DB_HOST = os.getenv("DB_HOST", default="oops")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname= DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(conn)

### A "cursor", a structure to iterate over db records to perform queries
curs = conn.cursor()

# create_table = '''
# CREATE TABLE test_table (
#   id        SERIAL PRIMARY KEY,
#   name  varchar(40) NOT NULL,
#   data    JSONB
# );
# '''

# insert_statement = '''
# INSERT INTO test_table (name, data) VALUES
# (
#   'A row name',
#   null
# ),
# (
#   'Another row, with JSON',
#   '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
# );
# '''
# #cur.execute(create_table)
# #cur.execute(insert_statement)
# conn.commit()

# query = '''
# SELECT * FROM test_table;
# '''
# cur.execute(query)
# result1 = cur.fetchall()
# print(result1)


