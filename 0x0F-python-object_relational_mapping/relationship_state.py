#!/usr/bin/python3
"""
Write a python file that contains the
class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    asd asd asd
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(128), nullable=False)
    
    cities = relationship('City', backref="state")

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# Base = declarative_base()


# class State(Base):
#     """Class state"""

#     __tablename__ = "states"

#     id = Column(Integer, nullable=False, primary_key=True)

#     name = Column(String(128), nullable=False)

#     cities = relationship("City", backref="state")
