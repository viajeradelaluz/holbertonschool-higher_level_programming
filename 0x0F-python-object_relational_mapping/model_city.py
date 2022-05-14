#!/usr/bin/python3
""" This module solves the following requirements and relies on the files
    ./14-model_city_fetch_by_state.py and task/14-model_city_fetch_by_state.sql

Write a Python file similar to model_state.py named model_city.py that contains
the class definition of a City:
    - City class:
        - inherits from Base (imported from model_state)
        - links to the MySQL table cities
        - class attribute id that represents a column of an auto-generated,
          unique integer, can't be null and is a primary key
        - class attribute name that represents a column of a string of 128
          characters and can't be null
        - class attribute state_id that represents a column of an integer,
          can't be null and is a foreign key to states.id
    - You must use the module SQLAlchemy
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City model that links to the table cities of 6-model_state.sql.
        """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
