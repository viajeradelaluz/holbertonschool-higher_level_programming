#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
    - You must use the packages requests and sys
    - You are not allow to import other packages than requests and sys
    - The value of this variable is different for each request
    - You don't need to check script arguments (number and type)
"""

from sys import argv
import requests


def main():
    html = requests.get(argv[1])
    print(html.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
