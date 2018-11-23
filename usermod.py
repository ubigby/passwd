#modify a user account

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

def mod_username():
    c.execute("UPDATE users SET username= (?) WHERE username= (?)", (username, new_username))

def mod_password():
   c.execute("UPDATE users SET username= (?) WHERE username= (?)", (password, new_password))
    
def mod_uid():
    c.execute("UPDATE users SET username= (?) WHERE username= (?)", (uid, new_uid))

    
print('Please enter a valid keyword to modify your account: username(n), password(p), uid(u)')
keyword = input()

if keyword == 'n':
    print('Please enter your current username:')
    username = str(input())
    print('Please enter your new username:')
    new_username = str(input())
    mod_username()
elif keyword == 'p':
    print('Please enter your current password:')
    password = int(input())
    print('Please enter your new password:')
    new_password = int(input())
    mod_password()
elif keyword == 'u':
    print('Please enter your current uid')
    uid = int(input())
    print('Please enter your new uid')
    new_uid = int(input())
    mod_uid()
else:
    print('Please retry with a valid keyword')


conn.commit()

conn.close()
