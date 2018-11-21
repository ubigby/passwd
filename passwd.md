# passwd

## Name

**passwd - password file**

## Description

The user account information is stored in the passwd.json file. The passwd utilities: useradd, userdel and usermod store the keys and values in a python dictionary object. The dictionary is then converted to a JSON string object.


| keys     | values |
| name     | string | 
| password | int    |
| UID      | int    |


## Example

```
}
    "name": "ump",
    "password": 123,
    "UID": 80
}
```
