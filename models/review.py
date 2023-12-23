#!/usr/bin/python3

"""
A module that defines ORM class for Review table
"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """
    Defines attributes for Review table
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship("User", backref="reviews", cascade="all, delete-orphan")

    
