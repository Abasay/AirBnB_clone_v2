#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """ returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            cities_dict = storage.all(City)
            return [obj for obj in cities_dict.values()
                    if obj.state_id == self.id]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
