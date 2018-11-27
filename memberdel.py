#delete a member 

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

# Create function for each member column.
username = input('Please enter your username to remove membership:\n')
groupname = input('Please enter your groupname:\n')
c.execute("UPDATE groups SET primary_member=null WHERE primary_member= (?) and groupname= (?)", (username, groupname))


conn.commit()

conn.close()    
