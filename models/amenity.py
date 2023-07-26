#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """
    Amenities Class representing amenities a place
    can offer
    """
    __tablename__ = 'amenities'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
