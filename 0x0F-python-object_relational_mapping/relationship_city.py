#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named
model_city.pythat contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """Class City"""
    
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(128), nullable=False)
    
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
