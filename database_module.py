import sqlite3
from cs50 import SQL  

DB = SQL("sqlite:///students.db")

def get_connection():
    return sqlite3.connect(DB)

connection = get_connection()
cursor = connection.cursor

return cursor.execute(f"SELECT * FROM Karen2556320")

def show_table(table_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    headers = [d[0] for d in cur.description]
    conn.close()

    print("\n--- TABLE:", table_name, "---")
    print(tabulate(rows, headers=headers, tablefmt="grid"))