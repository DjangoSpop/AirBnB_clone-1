<<<<<<< HEAD
#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3

"""
A module that defines the ORM class for Amenity table
"""
from os import getenv
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.place import place_amenity
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    """
    Defines Amenity class attributes
    """
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(60), nullable=False)
        place_amenities = relationship(
            'Place', secondary=place_amenity, viewonly=False
        )
    else:
        name = ''
>>>>>>> bba06fc45b17fc36c6d948c4d322dea98c3e6a01
