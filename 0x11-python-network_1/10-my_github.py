#!/usr/bin/python3
"""
Module that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
    - Use Basic Authentication with a personal access token as password to
      access to your information (only read:user permission is needed)
    - First argument will be your username
    - Second argument will be your password
    - You are not allowed to import packages other than requests and sys
    - You don't need to check arguments passed to the script (number or type)
"""

from sys import argv
import requests


def main():
    user, passwd = argv[1], argv[2]
    url = 'https://api.github.com/user'

    html = requests.get(url, auth=(user, passwd))
    print(html.json().get('id'))


if __name__ == '__main__':
    main()
