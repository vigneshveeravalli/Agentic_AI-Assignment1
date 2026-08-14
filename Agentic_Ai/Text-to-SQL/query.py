import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

query = """
SELECT c.name, SUM(o.amount) AS total_sales
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.name
"""

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()