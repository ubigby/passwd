#modify a user account

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

print('Please enter your username:')
username = str(input())

print('Please enter your password:')
password = int(input())

print('Please enter your uid')
uid = int(input())

# add password and uid, all modifications shou
c.execute("UPDATE users SET username= (?) WHERE username= (?)", (username, ))

conn.commit()

conn.close()
