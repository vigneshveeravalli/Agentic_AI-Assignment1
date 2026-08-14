import sqlite3

# Create/connect to database
connection = sqlite3.connect("database.db")

cursor = connection.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# Insert customers
customers = [
    (1, "Vishnu", "Hyderabad"),
    (2, "Rahul", "Delhi"),
    (3, "Priya", "Hyderabad"),
    (4, "Arun", "Mumbai"),
    (5, "Anjali", "Bangalore")
]

cursor.executemany(
    "INSERT OR IGNORE INTO customers VALUES (?, ?, ?)",
    customers
)

# Insert orders
orders = [
    (101, 1, "2025-01-10", 5000),
    (102, 1, "2025-02-15", 3000),
    (103, 2, "2025-03-20", 7000),
    (104, 3, "2025-04-10", 4000),
    (105, 4, "2025-05-12", 9000),
    (106, 5, "2025-06-18", 6000)
]

cursor.executemany(
    "INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?)",
    orders
)

connection.commit()
connection.close()

print("Database created successfully!")