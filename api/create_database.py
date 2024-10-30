import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    value TEXT              
)
""")


conn.close()