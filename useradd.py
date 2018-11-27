#create a user account

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()


username = input('Please enter a username:\n')
password = int(input('Please enter a password:\n'))
uid = int(input('Please enter a uid:\n'))

c.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, uid))

conn.commit()

conn.close()

