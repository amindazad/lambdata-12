import sqlite3

# Costruct a path to the database 
DB_FILEPATH = 'rpg_db.sqlite3'
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row

curs = conn.cursor()

print("How many total characters are there?")
query_1 = '''
SELECT 
	count(DISTINCT character_id) as characters_count
FROM charactercreator_character
'''
result1 = curs.execute(query_1).fetchall()
print('characters_count', result1)
#_______________________________________________

print("How many of each specific subclass?")

query_2 = '''
SELECT 
	count(DISTINCT character_ptr_id) as cleric_count
FROM charactercreator_cleric
'''
query_3 = '''
SELECT 
	count(DISTINCT character_ptr_id) as fighter_count
FROM charactercreator_fighter
'''
query_4 = '''
SELECT 
	count(DISTINCT character_ptr_id) as mage_count
FROM charactercreator_mage
'''
query_5 = '''
SELECT 
	count(DISTINCT character_ptr_id) as thief_count
FROM charactercreator_thief
'''
result2 = curs.execute(query_2).fetchall()
print('cleric_count', result2)
result3 = curs.execute(query_3).fetchall()
print('fighter_count', result3)
result4 = curs.execute(query_4).fetchall()
print('mage_count', result4)
result5 = curs.execute(query_5).fetchall()
print('thief_count', result5)

#_______________________________________________
print("How many total Items?")

query_6 = '''
SELECT 
	count(DISTINCT item_id) as item_count
FROM armory_item
'''
result6 = curs.execute(query_6).fetchall()
print('item_count', result6)
#_______________________________________________
print("How many of the items are weapon?")

query_7 = '''
SELECT 
	count(DISTINCT item_ptr_id) as weapon_count
FROM armory_weapon
'''
result7 = curs.execute(query_7).fetchall()
print('weapon_count', result7)

print("How many of the items are not weapon?")

query_9 = '''
SELECT 
	COUNT(item_id) as non_weapon_items
FROM armory_item
LEFT JOIN armory_weapon on armory_item.item_id = armory_weapon.item_ptr_id
WHERE armory_weapon.item_ptr_id is NULL
'''
result9 = curs.execute(query_9).fetchall()
print('non_weapon_count', result9)
for row in result1:
    print(type(row))
    print(row)
	print(row["non_weapon_items"])
    print("-----------")

#_______________________________________________
print("How many Items does each character have? (Return first 20 rows")

query_8 = '''
SELECT 
	character_id 
	,count(DISTINCT item_id) as item_count_per_character
FROM charactercreator_character_inventory
GROUP BY character_id
ORDER BY item_count_per_character DESC
LIMIT 20
'''
result8 = curs.execute(query_8).fetchall()
print('item_count_per_character', result8)
#_______________________________________________
print("How many weapons does each character have? (Return first 20 rows")

query_10 = '''
SELECT
	character_id, 
	COUNT(item_id) AS weapons_per_character
FROM charactercreator_character_inventory
INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
ORDER BY weapons_per_character DESC
LIMIT 20
'''
result10 = curs.execute(query_10).fetchall()
print('weapons_per_character', result10)
#_______________________________________________
print("On average, how many Items does each Character have?")

query_11 = '''
SELECT AVG(avg_item_count)
FROM(SELECT 
	character_id 
	,COUNT(DISTINCT item_id) as avg_item_count
FROM charactercreator_character_inventory
GROUP BY character_id
ORDER BY avg_item_count)
'''
result11 = curs.execute(query_11).fetchall()
print('avg_item_count', result11)
#_______________________________________________
print("On average, how many weapons does each Character have?")

query_11 = '''
SELECT AVG(avg_weapons) as avg_weapons
FROM(SELECT
	character_id, 
	COUNT(item_id) AS avg_weapons
FROM charactercreator_character_inventory
INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id
ORDER BY avg_weapons DESC)
'''
result11 = curs.execute(query_11).fetchall()
print('avg_weapons', result11)

#curs.execute(query)
result1 = curs.execute(query).fetchall()
print('result 1', result1)

for row in result1:
    print(type(row))
    print(row)
    print(row["Country"])
    print("-----------")
