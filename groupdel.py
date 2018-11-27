#delete a group account

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

groupname = input('Please enter the groupname to remove the account:\n')

c.execute("DELETE FROM groups WHERE groupname= (?)", (groupname,))

conn.commit()

conn.close()
