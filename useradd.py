#create a new user

import json

print('Please enter a username:')
user = str(input())
print('Please enter a password:')
passwd = int(input())
print('Please enter a uid:')
uid = int(input())

account = {'name': user, 'password': passwd, 'UID': uid}

with open('passwd.json', 'a') as file:
    json.dump(account, file, indent=4)
