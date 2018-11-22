#create a new user

import sqlite3

conn = sqlite3.connect('passwd.db')
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

