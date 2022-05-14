#!/usr/bin/python3
""" This module solves the following requirements and relies on the file
    task/7-model_state_fetch_all.sql

Write a script that changes the name of a State from the database hbtn_0e_6_usa
    - Take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state:
        from model_state import Base, State
    - Connect to a MySQL server running on localhost at port 3306
    - Change the name of the State where id = 2 to New Mexico
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

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == '__main__':
    main()
