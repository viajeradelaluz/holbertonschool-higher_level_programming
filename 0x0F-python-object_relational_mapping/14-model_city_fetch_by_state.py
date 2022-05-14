#!/usr/bin/python3
""" This module solves the following requirements and relies on the file
    task/14-model_city_fetch_by_state.sql

Write a script that prints all City objects from the database hbtn_0e_14_usa:
    - Take 3 arguments: mysql username, mysql password and database name
    - You must use the module SQLAlchemy
    - You must import State and Base from model_state:
        from model_state import Base, State
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - Results must be display as they are in the example below
        (<state name>: (<city id>) <city name>)
"""

from model_city import City
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

    cities_in_states = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for city, state in cities_in_states:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    main()
