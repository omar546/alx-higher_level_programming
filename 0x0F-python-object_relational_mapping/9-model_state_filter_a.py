#!/usr/bin/python3
"""List all states with 'a' via SQLAlchemy"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.mmekkawy/alx-higher_level_programming/0x0F-python-object_relational_mapping/7-model_state_fetch_all.pyetadata.create_all(engine)
    sessionMaker = sessionmaker(bind=engine)
    for state in sessionMaker().query(State).filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    sessionMaker().close()
    