#!/usr/bin/python3
""" This module solves the following requirements and relies on the file
    task/0-select_states.sql

Once again, write a script that takes in arguments and displays all values in the 
states table of hbtn_0e_0_usa where name matches the argument. But this time, 
write one that is safe from MySQL injections!
    - Take 4 arguments: mysql username, mysql password, database name
      and state name searched (safe from MySQL injection)
    - You must use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
"""

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3],
        host='localhost', port='3306')

    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM states WHERE name = "{}"'
        'ORDER BY id ASC'.format(argv[4]))

    states = cursor.fetchall()
    for state in states:
        if state[1] == 'N':
            print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
