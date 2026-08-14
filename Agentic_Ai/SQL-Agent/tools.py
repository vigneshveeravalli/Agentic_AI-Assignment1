import sqlite3


DATABASE = "database.db"


def list_tables():
    """Return all tables in the database."""

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%'
    """)

    tables = [row[0] for row in cursor.fetchall()]

    connection.close()

    return tables


def get_schema(table_name):
    """Return the schema of a table."""

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")

    columns = cursor.fetchall()

    connection.close()

    if not columns:
        return f"Table '{table_name}' does not exist."

    schema = []

    for column in columns:
        schema.append({
            "name": column[1],
            "type": column[2]
        })

    return schema


def execute_sql(query):
    """Execute a read-only SQL query."""

    query = query.strip()

    # Security: allow only SELECT
    if not query.upper().startswith("SELECT"):
        return "ERROR: Only SELECT queries are allowed."

    try:

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        columns = [
            description[0]
            for description in cursor.description
        ]

        connection.close()

        return {
            "columns": columns,
            "rows": rows
        }

    except Exception as e:

        return f"SQL ERROR: {str(e)}"