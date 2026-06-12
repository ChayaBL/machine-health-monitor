import sqlite3

conn = sqlite3.connect("machines.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT,
    machine_id TEXT,
    machine_type TEXT,
    health_score INTEGER,
    status TEXT,
    grade TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")