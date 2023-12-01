#!/usr/bin/env bash
# curl a URL and display the size of the response in bytes

curl -s "$1" | wc -c
