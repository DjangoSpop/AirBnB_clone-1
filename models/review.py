#!/usr/bin/python3
<<<<<<< HEAD
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
=======

"""
A module that defines ORM class for Review table
"""
from os import getenv
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
>>>>>>> bba06fc45b17fc36c6d948c4d322dea98c3e6a01
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
<<<<<<< HEAD
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship("User", backref="reviews", cascade="all, delete-orphan")

    
=======
    """
    Defines attributes for Review table
    """
    __tablename__ = 'reviews'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(
            String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ''
        place_id = ''
        user_id = ''
>>>>>>> bba06fc45b17fc36c6d948c4d322dea98c3e6a01
