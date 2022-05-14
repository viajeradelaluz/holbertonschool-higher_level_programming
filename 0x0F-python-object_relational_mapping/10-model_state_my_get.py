#!/usr/bin/python3
""" This module solves the following requirements and relies on the file
    task/7-model_state_fetch_all.sql

Write a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa:
    - Take 4 arguments: mysql username, mysql password, database name
      and state name to search (SQL injection free)
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state:
        from model_state import Base, State
    - Connect to a MySQL server running on localhost at port 3306
    - You can assume you have one record with the state name to search
    - Results must display the states.id
    - If no state has the name you searched for, display Not found
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print(state.id)
    else:
        print('Not found')

    session.close()


if __name__ == '__main__':
    main()
