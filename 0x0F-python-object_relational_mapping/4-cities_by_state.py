#!/usr/bin/python3
""" This module solves the following requirements and relies on the file
    task/4-cities_by_state.sql

Write a script that lists all cities from the database hbtn_0e_4_usa:
    - Take 3 arguments: mysql username, mysql password and database name
    - You must use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - You can use only execute() once
"""

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3],
        host='localhost', port=3306)

    cursor = db.cursor()
    cursor.execute(
        'SELECT cities.id, cities.name, states.name FROM cities '
        'JOIN states ON cities.state_id = states.id ORDER BY cities.id;'
    )

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
