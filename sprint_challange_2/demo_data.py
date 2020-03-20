import sqlite3

# Make a file path 
DB_FILEPATH = 'demo_data.sqlite3'

# Create a connection to the file path 
conn = sqlite3.connect(DB_FILEPATH)
# Create a cursor enabling us to execute queries
curs = conn.cursor()

# Create the demo table
demo = """
        CREATE TABLE demo(
        s TEXT,
        x INT,
        y INT);
"""

# Adding the table to the database 
curs.execute(demo).fetchall()

data = """
        INSERT INTO demo(s, x, y)
        VALUES ("g", 3, 9),
        ("v", 5, 7),
        ("f", 8, 7);
"""

# Adding the data to the demo table
curs.execute(data).fetchall()

# Closing the cursor and saving all the above using commit
curs.close()
conn.commit()

# Create a connection to the file path 
conn = sqlite3.connect(DB_FILEPATH)
# Create a cursor enabling us to execute queries
curs = conn.cursor()

# Count how many rows you have - it should be 3!

query = '''
SELECT count(*)
FROM demo
'''
result1 = curs.execute(query).fetchall()
print("number of rows:",result1)

# How many rows are there where both x and y are at least 5?
query_1 = '''
SELECT count(*)
FROM demo
WHERE x>=5
AND y>=5
'''
result2 = curs.execute(query_1).fetchall()
print("rows where both x and y are at least 5:",result2)

# How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
query_2 = '''
SELECT count(DISTINCT y)
FROM demo
'''
result3 = curs.execute(query_2).fetchall()
print("unique values of y:",result3)

# Create a function to produce all above (stretch goal)
def run(x, db="demo_data.sqlite3"):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.execute(x).fetchall()
    curs.close()
    conn.commit()
    return print(answer)

run(query)
run(query_1)
run(query_2)