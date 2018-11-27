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


keyword = input('Please enter a valid keyword to modify your user account: username(n), password(p), uid(u)\n')

if keyword == 'n':
    username = input('Please enter your current username:\n')
    new_username = input('Please enter your new username:\n')
    mod_username(new_username, username)
elif keyword == 'p':
    password = int(input('Please enter your current password:\n'))
    new_password = int(input('Please enter your new password:\n'))
    mod_password(new_password, password)
elif keyword == 'u':
    uid = int(input('Please enter your current uid:\n'))
    new_uid = int(input('Please enter your new uid:\n'))
    mod_uid(new_uid, uid)
else:
    print('Please retry with a valid keyword')


conn.commit()

conn.close()
