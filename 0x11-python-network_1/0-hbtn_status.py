#!/usr/bin/python3
"""
Module that fetches https://intranet.hbtn.io/status
    - You must use the package urllib
    - You are not allowed to import any packages other than urllib
    - You must use a with statement
"""

from urllib import request


def main():
    call = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(call) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))


if __name__ == '__main__':
    main()
