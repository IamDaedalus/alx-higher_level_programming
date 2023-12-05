#!/usr/bin/python3
""" this script fetches https://alx-intranet.hbtn.io/status with requests """

import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req.content.decode()))
