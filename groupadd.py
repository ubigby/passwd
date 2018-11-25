#create a group account

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

print('Please enter a groupname:')
groupname = str(input())

print('Please enter a group password:')
gpassword = int(input())

print('Please enter a gid:')
gid = int(input())

#usermod is used to add members to a group or modify group accounts
primary_member = None
secondary_member = None
teriary_member = None

c.execute("INSERT INTO groups VALUES (?, ?, ?, ?, ?, ?)", (groupname, gpassword, gid, primary_member, secondary_member, teriary_member))

conn.commit()

conn.close()
