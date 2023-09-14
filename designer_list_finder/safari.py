import sqlite3
from pathlib import Path

history_path = Path.home() / 'Library/Safari/History.db'
conn = sqlite3.connect(history_path)
cursor = conn.cursor()

cursor.execute("SELECT url FROM history_items")

with open("safari_history.txt", "w") as f:
    for row in cursor.fetchall():
        f.write(row[0] + "\n")
