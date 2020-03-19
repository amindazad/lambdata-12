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


# Load rpg data to postgresql
import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

row_count = '''SELECT COUNT(*) FROM charactercreator_character'''
result2 = sl_curs.execute(row_count).fetchall()
# print(result2)

#Step 1 extract the characters
get_characters = '''SELECT * FROM charactercreator_character'''
characters = sl_curs.execute(get_characters).fetchall()

#Step 2 Transform 
# We need a new table with the appropriate schema
# Getting the old schema 

old_schema = sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()
# print(old_schema)

# create_charactercreator_character = '''
# CREATE TABLE charactercreator_character (
#     character_id SERIAL PRIMARY KEY,
#     name VARCHAR(30),
#     level INT, 
#     exp INT, 
#     hp INT,
#     strenght INT,
#     intelligence INT,
#     dexterity INT,
#     wisdom INT
# );
# '''
# curs.execute(create_charactercreator_character)
# # conn.commit()

# ex_insert = '''
# INSERT INTO charactercreator_character
# (name, level, exp, hp, strenght, intelligence, dexterity, wisdom)
# VALUES ''' + str(get_characters[0][1:]) + ";"

for get_characters in get_characters:
    insert_character = '''
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strenght, intelligence, dexterity, wisdom)
    VALUES ''' + str(get_characters[1:]) + ";"
curs.execute(insert_character)
conn.commit()