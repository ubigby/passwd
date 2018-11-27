#add a member

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

print('Please enter your username account: ')
username = str(input())
print('Please enter a groupname: ')
groupname = str(input())
c.execute("UPDATE groups SET primary_member= (?) WHERE groupname= (?)", (username, groupname))


conn.commit()

conn.close()    
