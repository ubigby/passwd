#modify a group account

import sqlite3

conn = sqlite3.connect('groups.db')
c = conn.cursor()

def mod_groupname(x, y):
    c.execute("UPDATE groups SET groupname= (?) WHERE groupname= (?)", (x, y))

def mod_gpassword(x, y):
    c.execute("UPDATE groups SET gpassword= (?) WHERE gpassword= (?)", (x, y))
    
def mod_gid(x, y):
    c.execute("UPDATE groupss SET gid= (?) WHERE gid= (?)", (x, y))


print('Please enter a valid keyword to modify your group account: groupname(n), password(p), gid(g)')
keyword = input()

if keyword == 'n':
    groupname = input('Please enter your current groupname:\n')
    new_groupname = input('Please enter your new groupname:\n')
    mod_groupname(new_groupname, groupname)
elif keyword == 'p':
    gpassword = int(input('Please enter your current group password:\n'))
    new_gpassword = int(input('Please enter your new group password:\n'))
    mod_gpassword(new_gpassword, gpassword)
elif keyword == 'g':
    gid = int(input('Please enter your current gid:\n'))
    new_gid = int(input('Please enter your new gid:\n'))
    mod_gid(new_gid, gid)
else:
    print('Please retry with a valid keyword')


conn.commit()

conn.close()
