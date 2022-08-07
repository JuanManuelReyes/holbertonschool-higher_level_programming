#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named
model_city.pythat contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class City"""
    
    __tablename__ = 'cities'
    
    id = Column(Integer, nullable=False, primary_key=True)
    
    name = Column(String(128), nullable=False)
    
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)