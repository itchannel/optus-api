import sys

from optus import Account


if len(sys.argv) < 3:
    raise Exception('Must specify Username, Password and phone number as arguments, e.g. demo.py test@test.com password123 04123456')

acc = Account(sys.argv[1], sys.argv[2], sys.argv[3])

print(acc.usage())
# print(acc.addons())
# print(acc.geofencing())
