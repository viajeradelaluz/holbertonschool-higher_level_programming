#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
    - You must use the packages urllib and sys
    - You are not allow to import packages other than urllib and sys
    - The value of this variable is different for each request
    - You dont need to check arguments passed to the script (number or type)
    - You must use a with statement
"""

from sys import argv
from urllib import request


def main():
    call = request.Request(argv[1])
    with request.urlopen(call) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
