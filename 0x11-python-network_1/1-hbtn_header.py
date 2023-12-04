#!/usr/bin/python3
""" display the x-request-id header variable of a request to a URL"""

import urllib.request
from sys import argv as av

if __name__ == "__main__":
    with urllib.request.urlopen(av[1]) as req:
        print(req.getheader('x-request-id'))
