#!/usr/bin/python3
"""Defines a City model that Inherits Base (SQLAlchemy)"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """Represents a MySQL database City.

    Attrs:
        id (sqlalchemy.Column): city's id.
        name (sqlalchemy.Column): city's name.
        state_id (sqlalchemy.Column): city-state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
