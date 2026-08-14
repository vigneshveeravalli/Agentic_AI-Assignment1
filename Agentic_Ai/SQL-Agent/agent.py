
import requests

from tools import (
    list_tables,
    get_schema,
    execute_sql
)


MODEL = "llama3.2"


def ask_llm(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]


def agent(question):

    print("\nUSER:")
    print(question)

    # ----------------------------------------
    # STEP 1: Get available tables
    # ----------------------------------------

    tables = list_tables()

    print("\nTOOL: list_tables()")
    print("RESULT:", tables)

    # ----------------------------------------
    # STEP 2: Get schemas
    # ----------------------------------------

    schemas = {}

    for table in tables:

        schemas[table] = get_schema(table)

        print(f"\nTOOL: get_schema({table})")
        print("RESULT:", schemas[table])

    # ----------------------------------------
    # STEP 3: Ask LLM to generate SQL
    # ----------------------------------------

    prompt = f"""
You are a ReAct SQL agent.

You have access to a SQLite database.

Tables:
{tables}

Schemas:
{schemas}

User question:
{question}

Think about which tables and columns are needed.

Then generate ONE SQLite SELECT query.

Rules:
- Only generate SELECT queries.
- Do not INSERT.
- Do not UPDATE.
- Do not DELETE.
- Do not DROP.
- Use only the tables and columns provided.

Return ONLY the SQL query.
"""

    sql = ask_llm(prompt).strip()

    # Remove markdown code fences if the LLM adds them
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    print("\nAGENT ACTION:")
    print(sql)

    # ----------------------------------------
    # STEP 4: Execute SQL
    # ----------------------------------------

    result = execute_sql(sql)

    print("\nTOOL: execute_sql()")
    print("RESULT:", result)

    # ----------------------------------------
    # STEP 5: Generate final answer
    # ----------------------------------------

    final_prompt = f"""
You are a helpful database assistant.

User question:
{question}

SQL query:
{sql}

Database result:
{result}

Answer the user's question using the database result.

Do not mention internal tools.
Give a short and clear answer.
"""

    answer = ask_llm(final_prompt)

    return answer