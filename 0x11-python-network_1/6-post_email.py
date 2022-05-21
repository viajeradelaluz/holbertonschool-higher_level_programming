#!/usr/bin/python3
"""
Module that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body of
the response.
    - The email must be sent in the variable email
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don't need to error check arguments passed to the script

Please test your script in the sandbox provided, using the web server
running on port 5000
"""

from sys import argv
import requests


def main():
    email = {'email': argv[2]}
    html = requests.post(argv[1], email)
    print(html.text)


if __name__ == '__main__':
    main()
