#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
and displays the body of the response """

from urllib import request, error
from sys import argv as av


if __name__ == "__main__":
    with request.urlopen(av[1]) as req:
        try:
            print("{}".format(req.read().decode('utf-8')))
        except error.HTTPError as e:
            print("Error code: {}".format(e.reason))
