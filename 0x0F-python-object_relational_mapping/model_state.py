#!/usr/bin/python3
""" This module solves the following requirements and relies on the files
    ./6-model_state.py and task/6-model_state.sql

Write a python file that contains the class definition of a State and
an instance Base = declarative_base():
    - State class:
        - inherits from Base Tips
        - links to the MySQL table states
        - class attribute id that represents a column of an auto-generated,
          unique integer, can't be null and is a primary key
        - class attribute name that represents a column of a string
          with maximum 128 characters and can't be null
    - You must use the module SQLAlchemy
    - Connect to a MySQL server running on localhost at port 3306
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State model that links to the table states of 6-model_state.sql.
        """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=True)
