#modify a user account

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

def mod_username(x, y):
    c.execute("UPDATE users SET username= (?) WHERE username= (?)", (x, y))

def mod_password(x, y):
   c.execute("UPDATE users SET password= (?) WHERE password= (?)", (x, y))
    
def mod_uid(x, y):
    c.execute("UPDATE users SET uid= (?) WHERE uid= (?)", (x, y))

    
print('Please enter a valid keyword to modify your user account: username(n), password(p), uid(u)')
keyword = input()

if keyword == 'n':
    print('Please enter your current username:')
    username = str(input())
    print('Please enter your new username:')
    new_username = str(input())
    mod_username(new_username, username)
elif keyword == 'p':
    print('Please enter your current password:')
    password = int(input())
    print('Please enter your new password:')
    new_password = int(input())
    mod_password(new_password, password)
elif keyword == 'u':
    print('Please enter your current uid')
    uid = int(input())
    print('Please enter your new uid')
    new_uid = int(input())
    mod_uid(new_uid, uid)
else:
    print('Please retry with a valid keyword')


conn.commit()

conn.close()
