import requests


defaultHeaders = {
    "Accept": "application/json",
    "User-Agent": "User-Agent: My Optus 6.7.5243 (iOS 13.4)",
    "Authorization": "Basic bXlvcHR1cy1tczpPdWF0dHdUQix3bHRpYWhvdG8saWF3Lk9vdHdhTCxTLFdCO2Fvd2FNQixhdG93YUcsSEIu"
}


class Account(object):

    def __init__(self, username, password, number):
        self.username = username
        self.password = password
        self.number = number
        self.token = None
        self.expires = None
        self.expiresAt = None
        self.refresh_token = None
        self.saveToken = False

    def auth(self):

        data = {
            "scope": "ACCOUNT",
            "username": self.username,
            "password": self.password,
            "grant_type": "register",
        }

        headers = {
            **defaultHeaders
        }

        r = requests.post(
            "https://moa.optusnet.com.au/myoptus/oauth/token",
            data=data,
            headers=headers
        )
        
        if r.status_code == 400:
            raise Exception("Incorrect Credentials")

        if r.status_code == 200:
            result = r.json()
            self.token = result["access_token"]
            return True

    def usage(self):

        self.__acquireToken()

        headers = {
            **defaultHeaders,
            "Authorization": "Bearer " + self.token

        }

        r = requests.get(
            "https://moa.optusnet.com.au/myoptus/api/usages/v2/serviceid/" + self.number,
            headers=headers
        )
        if r.status_code == 401:
            raise Exception(r.text)
        if r.status_code == 200:
            return r.json()

    def addons(self):

        self.__acquireToken()

        headers = {
            **defaultHeaders,
            "Authorization": "Bearer " + self.token

        }

        r = requests.get(
            "https://moa.optusnet.com.au/myoptus/api/services/" + self.number + "/addons",
            headers=headers
        )

        if r.status_code == 200:
            return r.json()

    def geofencing(self):
        self.__acquireToken()

        headers = {
            **defaultHeaders,
            "Authorization": "Bearer " + self.token

        }

        r = requests.get(
            "https://moa.optusnet.com.au/myoptus/api/geofence/fencelist/v2",
            headers=headers
        )

        if r.status_code == 200:
            return r.json()

    def __acquireToken(self):

        if self.token is None:
            # No existing token exists so refreshing library
            self.auth()
        else:
            # logging.info("Token is valid, continuing")
            pass
