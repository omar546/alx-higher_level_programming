#!/usr/bin/python3
"""list all state objects - sqlalchemy"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    maker = sessionmaker(bind=eng)
    session = maker()
    states = session.query(State)\
                    .filter(State.name.contains('a'))\
                    .order_by(State.id)
    if (states is not None):
        for state in states:
            print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
