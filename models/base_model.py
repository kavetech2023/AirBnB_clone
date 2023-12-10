#!/usr/bin/python3
"""
BaseModel Module Definition
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class definition
    """
    def __init__(self, *args, **kwargs):
        """ BaseModel initialisation """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        tformat = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tformat)
                else:
                    self.__dict__[key] = value

        models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """
        string representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
