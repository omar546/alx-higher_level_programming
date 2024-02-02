#!/usr/bin/python3
"""Defines a State model that Inherits Base (SQLAlchemy)"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents a MySQL database [state]

    Attrs:
        __tablename__ (str): name of the States table.
        id (sqlalchemy.Integer): state's id.
        name (sqlalchemy.String): state's name.
        cities (sqlalchemy.orm.relationship): relationship of City-State.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
