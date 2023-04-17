#!/usr/bin/python3

"""
Class Definition of a City and an instance of Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """
    Represents a state for MySQL Database.

    __tablename__ (str): name of the MySQL table to store State
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): the state's name
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)