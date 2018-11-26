
import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

c.execute("SELECT * FROM groups")

for row in c.fetchall():
    print(row)
