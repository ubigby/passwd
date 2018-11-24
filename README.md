# pass-utils

## Description
- Utilities for managing accounts and passwords wriiten in python 3.
- The account information is stored in databases using sqlite.

## Tasks
- groups.db groups database
- groupadd create a group account
- groupdel delete a group account
- groupmod modify a group account
- lsgroups list groups database
- docs

## Completed
- users.db user database
- useradd create a user account
- userdel delete a user account
- usermod modify a user account
- lsusers list users database

## Future
- encryption
- passwords.db passwords database

## Databases
- users (username TEXT, password INT, uid INT)
- groups (groupname TEXT, gpassword INT, gid INT)

## Docs
- [useradd](https://github.com/ubigby/passwd/blob/master/useradd.md)
- [userdel](https://github.com/ubigby/passwd/blob/master/userdel.md)
- [usermod](https://github.com/ubigby/passwd/blob/master/usermod.md)
