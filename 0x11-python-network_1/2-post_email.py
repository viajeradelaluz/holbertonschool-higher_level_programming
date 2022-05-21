#!/usr/bin/python3
"""
Module that takes in a URL and an email, sends a POST request with the email as
a parameter, and displays the body of the response (decoded in utf-8)
    - The email must be sent in the email variable
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - You don't need to check arguments passed to the script (number or type)
    - You must use the with statement
Please test your script in the sandbox provided, using the web server
running on port 5000
"""

from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def main():
    call = Request(argv[1])
    email = urlencode({'email': argv[2]}).encode('utf-8')
    with urlopen(call, email) as body:
        print(body.read().decode('utf-8'))


if __name__ == '__main__':
    main()
