#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response """

from urllib import request, parse
from sys import argv as av


if __name__ == "__main__":
    email = av[2]
    data = parse.urlencode({"email": email}).encode()
    link = av[1]
    send = request.Request(link, data)

    with request.urlopen(send) as resp:
        print("{}".format(resp.read().decode('utf-8')))
