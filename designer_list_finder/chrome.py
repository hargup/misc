import sqlite3
import os

path = os.path.expandvars('/Users/harshwork/Library/Application Support/Google/Chrome/Default/History')
conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
cursor = conn.cursor()

cursor.execute("SELECT url, title, last_visit_time FROM urls")

with open("chrome_history.txt", "w") as f:
    for row in cursor.fetchall():
        f.write(f"{row[0]} | {row[1]} | {row[2]}\n")