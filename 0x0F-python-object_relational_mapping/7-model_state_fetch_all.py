#!/usr/bin/python3
"""List all states via SQLAlchemy"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sessionMaker = sessionmaker(bind=engine)
    for state in sessionMaker().query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    sessionMaker().close()
    