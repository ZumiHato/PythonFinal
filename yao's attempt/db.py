import sqlite3
from datetime import datetime, timedelta

DB = "students.db"

def get_connection():
    return sqlite3.connect(DB)

def create_student_table(student_name, student_id):
    table_name = student_name + student_id

    conn = get_connection()
    cur = conn.cursor()

    start_date = datetime(2025, 11, 17)
    time_slots = ["12", "34", "56", "78"]

    rows = []

    for day_number in range(5):
        current_day = start_date + timedelta(days=day_number)
        day_string = current_day.strftime("%Y-%m-%d")

        for slot in time_slots:
            date_time_slot = day_string + "-" + slot
            rows.append((date_time_slot, None, None, None, None, None, None))

    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cur.fetchone()[0]
  
    if row_count == 0:
        cur.executemany(
            f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?)",
            rows
        )

    conn.commit()
    conn.close()

    return table_name
