#delete a user account

import json

print('Please enter your username:')
user = str(input())
print('Please enter your password:')
passwd = int(input())
print('Please enter your uid:')
uid = int(input())


with open('passwd.json', 'r') as file:
    data = json.load(file)
    if data['name'] == user and data['password'] == passwd and data['UID'] == uid:
        del data['name']
        del data['password']
        del data['UID']
    else:
        print(type(data))
        

