#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Represents an amenity data set."""
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
    )
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
