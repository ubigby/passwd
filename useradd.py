#create a new user

print('Please enter a username:')
user = str(input())
print('Please enter a password:')
passwd = int(input())
print('Please enter a uid')
uid = int(input())

f = open('passwd.txt', 'a')
f.write('{}:{}:{}\n'.format(user, passwd, uid))
f.close()
