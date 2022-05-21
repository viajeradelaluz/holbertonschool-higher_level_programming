#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL and displays the body
of the response.
    - If the HTTP status code is greater than or equal to 400, print:
        Error code: followed by the value of the HTTP status code
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don't need to check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server
running on port 5000
"""

from sys import argv
import requests


def main():
    html = requests.get(argv[1])
    if html.status_code >= 400:
        print('Error code: {}'.format(html.status_code))
    else:
        print(html.text)


if __name__ == '__main__':
    main()
