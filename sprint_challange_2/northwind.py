import sqlite3
# Make a file path 
DB_FILEPATH = 'northwind_small.sqlite3'
# Create a connection to the file path 
conn = sqlite3.connect(DB_FILEPATH)
# Create a cursor enabling us to execute queries
curs = conn.cursor()

# Loading and looking at the tables
tables = curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
print(tables)
# list of tables :
# [('Category',), ('Customer',), ('CustomerCustomerDemo',),
# ('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
# ('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
# ('Territory',)]

# What are the ten most expensive items (per unit price) in the database?
query = '''
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
'''
result1 = curs.execute(query).fetchall()
print("ten most expensive items (per unit price):",result1)

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
query_1 = '''
SELECT AVG(HireDate - BirthDate)
FROM Employee
'''
result2 = curs.execute(query_1).fetchall()
print("average age of an employee at the time of their hiring:",result2)

# (Stretch) How does the average age of employee at hire vary by city?
query_2 = '''
SELECT AVG(HireDate - BirthDate), City
FROM Employee
WHERE City = "Seattle"
'''
result3 = curs.execute(query_2).fetchall()
print("average age of employee at Seattle:",result3)

query_3 = '''
SELECT AVG(HireDate - BirthDate), City
FROM Employee
WHERE City = "Tacoma"
'''
result4 = curs.execute(query_3).fetchall()
print("average age of employee at Tacoma:",result4)

query_4 = '''
SELECT AVG(HireDate - BirthDate), City
FROM Employee
WHERE City = "Kirkland"
'''
result5 = curs.execute(query_4).fetchall()
print("average age of employee at Kirkland:",result5)

query_5 = '''
SELECT AVG(HireDate - BirthDate), City
FROM Employee
WHERE City = "London"
'''
result6 = curs.execute(query_5).fetchall()
print("average age of employee at Kirkland:",result6)

query_6 = '''
SELECT AVG(HireDate - BirthDate), City
FROM Employee
WHERE City = "Redmond"
'''
result7 = curs.execute(query_6).fetchall()
print("average age of employee at Kirkland:",result7)

#What are the ten most expensive items (per unit price) in the database and their suppliers?
query_7 = '''
SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
'''
result8 = curs.execute(query_7).fetchall()
print("ten most expensive items (per unit price) per suppliers:",result8)

# What is the largest category (by number of unique products in it)?
query_8 = '''
SELECT CategoryName
FROM Product
JOIN Category ON Product.CategoryId = Category.Id
GROUP BY CategoryName 
ORDER BY COUNT(Distinct ProductName) DESC
LIMIT 1 
'''
result9 = curs.execute(query_8).fetchall()
print("largest category (by number of unique products in it):",result9)

# (Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.
query_9 = '''
SELECT EmployeeId, COUNT(DISTINCT TerritoryId), LastName
FROM EmployeeTerritory
JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id
GROUP BY EmployeeId
ORDER BY COUNT(DISTINCT TerritoryId) DESC
LIMIT 1
'''
result10 = curs.execute(query_9).fetchall()
print("employee with the most territories:",result10)

# Create a function to produce all above (stretch goal)
def run(x, db="northwind_small.sqlite3"):
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
run(query_3)
run(query_4)
run(query_5)
run(query_6)
run(query_7)
run(query_8)
run(query_9)

curs.close()
conn.commit()



