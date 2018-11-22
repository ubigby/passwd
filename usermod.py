#modify a user account

import fileinput

print('Please enter your username:')
user = str(input())
print('Please enter your password:')
passwd = int(input())
print('Please enter your uid')
uid = int(input())
print('Please enter your new username:')
newUser = str(input())
print('Please enter your new password:')
newPasswd = int(input())
print('Please enter your new uid')
newUid = int(input())

for line in fileinput.input('passwd.txt', inplace=True):
    line.replace('{}:{}:{}\n'.format(user, passwd, uid), '{}:{}:{}\n'.format(newUser, newPasswd, newUid))
