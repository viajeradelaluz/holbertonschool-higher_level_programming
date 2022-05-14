#!/usr/bin/env python3
""" This module solves the following requirements and relies on the file
    task/0-select_states.sql

Write a script that lists all states from hbtn_0e_0_usa (db):
    - Take 3 arguments: mysql username, mysql password and database name
    - You must use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
"""

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3],
        host='localhost', port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
