# Optus Mobile API Integration

This is a python wrapper for the Optus mobile API. It provides the ability to view account usage information and other capabilities normally only accessed via the mobile application. 

**Base64 auth is a generic token for the Optus API and does not contain credentials**


## Features

* Usage Information (Balance, data remaining etc)
* Addon information (Details of addons applied or avaliable for the account)
* Geofencing Information (Geofences that have been configured for the account)

## Install

Install using pip:
```
pip install optus
```


## Demo
To test the script there is a demo script that can be used
```
demo.py EMAIL PASSWORD MOBILE
```

Example
```
demo.py test@test.com password1 04123456
```

## Library Usage
Simple Usage
```
from optus import Account
acc = Account("email", "password", "mobile")
print(acc.usage())
```