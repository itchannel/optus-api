# Optus Mobile API Integration

**Base64 auth is a generic token for the Optus API and does not contain credentials**

This python script interacts with the Optus mobile API to allow for returning of stats like usage data, tracking metrics and addons. 


## Usage

Simple Usage
``` 
from optus import Account

acc = Account("email", "password", "mobile")

print(acc.usage())
```