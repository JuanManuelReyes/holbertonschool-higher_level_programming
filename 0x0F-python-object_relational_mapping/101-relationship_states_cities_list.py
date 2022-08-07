#!/usr/bin/python3
"""
write a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{states.id}: {states.name}")
        for cities in states.cities:
            print(f"    {cities.id}: {cities.name}")

    session.close()
