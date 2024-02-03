#!/usr/bin/python3
"""
Defines a city model
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """city for a MySQL database.
    Attributes:
        id (str): id.
        name (sqlalchemy.Integer): name.
        state_id (sqlalchemy.String):state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
