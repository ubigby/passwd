#create a user account

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

print('Please enter a username:')
username = str(input())

print('Please enter a password:')
password = int(input())

print('Please enter a uid:')
uid = int(input())

c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, uid))

conn.commit()

conn.close()

