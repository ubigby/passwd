# pass-utils

## Description
- Utilities for managing accounts and passwords written in python 3.
- The account information is stored in databases using sqlite 3.

## Dependencies 

- All commands depends on the tables existing, you can create the tables with create_tables script.

## Completed
- users.db user database
- useradd create a user account
- userdel delete a user account
- usermod modify a user account
- lsusers list users database
- groups.db groups database
- groupadd create a group account
- groupdel delete a group account
- groupmod modify a group account
- lsgroups list groups database
- memberadd add a member to a group account
- memberdel delete a member from a group account

## Future
- encryption
- GUI 

## Databases
- users (username TEXT, password INT, uid INT)
- groups (groupname TEXT, gpassword INT, gid INT, primary_member text, secondary_member text, tertiary_member text)

## Docs
- [useradd](https://github.com/ubigby/passwd/blob/master/useradd.md)
- [userdel](https://github.com/ubigby/passwd/blob/master/userdel.md)
- [usermod](https://github.com/ubigby/passwd/blob/master/usermod.md)
- [groupadd](https://github.com/ubigby/passwd/blob/master/groupadd.md)
- [groupdel](https://github.com/ubigby/passwd/blob/master/groupdel.md)
- [groupmod](https://github.com/ubigby/passwd/blob/master/groupmod.md)
