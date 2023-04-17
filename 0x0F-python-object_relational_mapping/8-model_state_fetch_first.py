#!/usr/bin/python3

"""
Script that prints the first State object from the
database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

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

    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

