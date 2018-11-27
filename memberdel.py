#delete a member 

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

print('Please enter your username to remove membership: ')
username = str(input())
print('Please enter your groupname: ')
groupname = str(input())
c.execute("UPDATE groups SET primary_member=null WHERE primary_member= (?) and groupname= (?)", (username, groupname))


conn.commit()

conn.close()    
