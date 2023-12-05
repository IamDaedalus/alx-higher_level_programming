#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response """

import requests
from sys import argv as av


if __name__ == "__main__":
    email = av[2]
    data = {"email": email}
    link = av[1]
    send = requests.post(link, data)

    print("{}".format(send.text))
