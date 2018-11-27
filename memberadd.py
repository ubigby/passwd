#add a member

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

# Create function for each member column.
username = input('Please enter your username account:\n')
groupname = input('Please enter a groupname:\n')
c.execute("UPDATE groups SET primary_member= (?) WHERE groupname= (?)", (username, groupname))


conn.commit()

conn.close()    
