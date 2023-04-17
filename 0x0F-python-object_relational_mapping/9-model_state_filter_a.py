#!/usr/bin/python3

"""
Lists all State objects that contain the letter a from the
database hbtn_0e_6_usa

This script takes 3 arguments:
    -- mysql username
    -- mysql password
    -- database name
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine(
    f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}",
        pre_pool_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).filter(State.name.like('%a%')):
        print(f"{state.id}: {state.name}")
