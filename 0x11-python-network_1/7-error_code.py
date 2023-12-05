#!/usr/bin/python3
""" this takes in a URL, sends a request to the URL
and displays the body of the response """

import requests
from sys import argv as av


if __name__ == "__main__":
    req = requests.get(av[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print("{}".format(req.content))
