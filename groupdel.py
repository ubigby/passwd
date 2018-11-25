#delete a group account

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

print('Please enter the groupname to remove the account:')
groupname = str(input())

c.execute("DELETE FROM groups WHERE groupname= (?)", (groupname,))

conn.commit()

conn.close()
