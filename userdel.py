#delete a user account

import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()


username = input('Please enter your username to remove the account:\n')

c.execute("DELETE FROM users WHERE username= (?)", (username,))

conn.commit()

conn.close()


