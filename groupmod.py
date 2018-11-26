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
    print('Please enter your current groupname:')
    groupname = str(input())
    print('Please enter your new groupname:')
    new_groupname = str(input())
    mod_groupname(new_groupname, groupname)
elif keyword == 'p':
    print('Please enter your current group password:')
    gpassword = int(input())
    print('Please enter your new group password:')
    new_gpassword = int(input())
    mod_gpassword(new_gpassword, gpassword)
elif keyword == 'g':
    print('Please enter your current gid')
    gid = int(input())
    print('Please enter your new gid')
    new_gid = int(input())
    mod_gid(new_gid, gid)
else:
    print('Please retry with a valid keyword')


conn.commit()

conn.close()
