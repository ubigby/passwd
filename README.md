# pass-utils

## Description
- Utilities for managing accounts and passwords wriiten in python 3.
- The account information is stored in databases using sqlite.

## Tasks
- groupmod modify a group account
- lsgroups list groups database
- docs

## Completed
- users.db user database
- useradd create a user account
- userdel delete a user account
- usermod modify a user account
- lsusers list users database
- groups.db groups database
- groupadd create a group account
- groupdel delete a group account

## Future
- encryption
- passwords.db passwords database

## Databases
- users (username TEXT, password INT, uid INT)
- groups (groupname TEXT, gpassword INT, gid INT, primary_member text, secondary_member text, teriary_member text)

## Docs
- [useradd](https://github.com/ubigby/passwd/blob/master/useradd.md)
- [userdel](https://github.com/ubigby/passwd/blob/master/userdel.md)
- [usermod](https://github.com/ubigby/passwd/blob/master/usermod.md)
- [groupadd](https://github.com/ubigby/passwd/blob/master/groupadd.md)
- [groupdel](https://github.com/ubigby/passwd/blob/master/groupdel.md)
- [groupmod](https://github.com/ubigby/passwd/blob/master/groupmod.md)
