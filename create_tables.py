#create databases
 
import sqlite3

def create_users_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("CREATE TABLE users (username text, password integer, uid integer)")
    conn.commit()
    conn.close()
    
def create_groups_table():
    conn = sqlite3.connect('groups.db')
    c = conn.cursor()
    c.execute("CREATE TABLE groups (groupname text, gpassword integer, gid integer, primary_member text, secondary_member text, tertiary_member text)")
    conn.commit()
    conn.close()


create_users_table()
create_groups_table()


