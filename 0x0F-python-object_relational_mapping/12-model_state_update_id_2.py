#!/usr/bin/python3

"""
Prints the State object with the name passed as an
argument from the database hbtn_0e_usa

The script takes 4 arguments:
    -- mysql username
    -- mysql password
    -- database name
    -- state name to search
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
name_passed = sys.argv[4]

if __name__ == "__main__":
    engine = create_engine(
    f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}",
        pre_pool_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
