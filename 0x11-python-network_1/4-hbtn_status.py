#!/usr/bin/python3
"""
Module that fetches https://intranet.hbtn.io/status
    - You must use the package requests
    - You are not allow to import packages other than requests
"""

import requests


def main():
    html = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(html.text)))
    print('\t- content: {}'.format(html.text))


if __name__ == '__main__':
    main()
