#!/usr/bin/python3
""" this script requests a specific header using requests """

import requests
from sys import argv as av


if __name__ == "__main__":
    req = requests.get(av[1])
    print("{}".format(req.headers['x-request-id']))
