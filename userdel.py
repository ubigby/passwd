#delete a user account

import sqlite3

conn = sqlite3.connect('passwd.db')
c = conn.cursor()

print('Please enter your username to remove your account:')
username = str(input())

c.execute("DELETE FROM users WHERE username= (?)", (username,))

conn.commit()

conn.close()


