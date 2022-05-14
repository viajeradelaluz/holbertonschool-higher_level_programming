#!/usr/bin/python3
""" Start link class to table in database. Please take a look to the
    model_state.py to see the entire task.
    """

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv


def main():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
