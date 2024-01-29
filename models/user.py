#!/usr/bin/python3
<<<<<<< HEAD
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
=======

"""
A module that defines the ORM class for User table
"""
from os import getenv
from models.base_model import Base, BaseModel
>>>>>>> bba06fc45b17fc36c6d948c4d322dea98c3e6a01
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
=======
    """
    Defines attributes for User table
    """
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
>>>>>>> bba06fc45b17fc36c6d948c4d322dea98c3e6a01
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
=======
        places = relationship(
            'Place', backref='user', cascade='all, delete')
        reviews = relationship(
            'Review', backref='user', cascade='all, delete')
        
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
>>>>>>> bba06fc45b17fc36c6d948c4d322dea98c3e6a01
