#!/usr/bin/python3
""" this script displays my GitHub id """

import requests
from requests.auth import HTTPBasicAuth
from sys import argv as av

if __name__ == "__main__":
    # https://datagy.io/python-requests-authentication/
    auth = HTTPBasicAuth(av[1], av[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
