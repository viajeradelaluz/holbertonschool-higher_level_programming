#!/usr/bin/python3
"""
Module that fetches https://intranet.hbtn.io/status
    - You must use the package urllib
    - You are not allowed to import any packages other than urllib
    - You must use a with statement
"""

from urllib import request


def main():
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print(
            'Body response:\n'
            '\t- type: {}\n'.format(type(html)),
            '\t- content: {}\n'.format(html),
            '\t- utf8 content: {}'.format(html.decode('utf8'))
        )


if __name__ == '__main__':
    main()
