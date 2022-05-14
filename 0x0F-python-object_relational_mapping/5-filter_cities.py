#!/usr/bin/python3
""" This module solves the following requirements and relies on the file
    task/4-cities_by_state.sql

Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa:
    - Take 4 arguments: mysql username, mysql password database name and
      state name (SQL injection free!)
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
        'SELECT cities.name FROM cities '
        'JOIN states ON cities.state_id = states.id '
        'WHERE states.name LIKE %s ORDER BY cities.id ASC;', (argv[4], ))

    cities = cursor.fetchall()
    print(', '.join(city[0] for city in cities))

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
