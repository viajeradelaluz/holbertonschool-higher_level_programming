#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
    - You have to manage urllib.error.HTTPError exceptions and print:
        Error code: followed by the HTTP status code
    - You must use the packages urllib and sys
    - You are not allowed to import other packages than urllib and sys
    - You don't need to check arguments passed to the script (number or type)
    - You must use the with statement
Please test your script in the sandbox provided, using the web server
running on port 5000
"""

from sys import argv
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def main():
    try:
        call = Request(argv[1])
        with urlopen(call) as body:
            print(body.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))


if __name__ == '__main__':
    main()
