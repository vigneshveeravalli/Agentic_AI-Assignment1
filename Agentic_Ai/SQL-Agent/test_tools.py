from tools import list_tables, get_schema, execute_sql


print("TABLES:")
print(list_tables())

print("\nCUSTOMERS SCHEMA:")
print(get_schema("customers"))

print("\nSQL RESULT:")
print(
    execute_sql(
        "SELECT * FROM customers"
    )
)