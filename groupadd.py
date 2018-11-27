#create a group account

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()


groupname = input('Please enter a groupname:\n')
gpassword = int(input('Please enter a group password:\n'))
gid = int(input('Please enter a gid:\n'))

#groupmod is used to add members to a group or modify group accounts
primary_member = None
secondary_member = None
tertiary_member = None

c.execute("INSERT INTO groups VALUES (?, ?, ?, ?, ?, ?)", (groupname, gpassword, gid, primary_member, secondary_member, tertiary_member))

conn.commit()

conn.close()
