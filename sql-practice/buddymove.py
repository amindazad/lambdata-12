import pandas as pd
import sqlite3

df = pd.read_csv('https://raw.githubusercontent.com/amindazad/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

DB_FILEPATH = 'buddymove_holidayiq.sqlite3'
conn = sqlite3.connect(DB_FILEPATH)
# conn.row_factory = sqlite3.Row
curs = conn.cursor()

#df.to_sql('review', con=conn)

query_1 = '''
SELECT count() 
FROM review
'''
curs.execute(query_1)
result1 = curs.execute(query_1).fetchall()
print("No of rows:", result1)

query_2 = '''
SELECT count() as users_100
FROM review
WHERE Nature >= 100 AND Shopping >= 100
'''
curs.execute(query_2)
result2 = curs.execute(query_2).fetchall()
print("Number of users more than 100 for nature and shopping:", result2)

query_3 = '''
SELECT AVG(sports_no) FROM(SELECT 
	count(Sports) AS sports_no 
FROM review)
'''
curs.execute(query_3)
result3 = curs.execute(query_3).fetchall()
print("Average number of Sports reviews:", result3)

query_4 = '''
SELECT AVG(religous_no) FROM(SELECT 
	count(Religious) AS religous_no 
FROM review)
'''
curs.execute(query_4)
result4 = curs.execute(query_4).fetchall()
print("Average number of Religous reviews:", result4)

query_5 = '''
SELECT AVG(nature_no) FROM(SELECT 
	count(Nature) AS nature_no 
FROM review)
'''
curs.execute(query_5)
result5 = curs.execute(query_5).fetchall()
print("Average number of Nature reviews:", result5)


