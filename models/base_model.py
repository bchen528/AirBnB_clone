#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime

"""Base Module for all Objects"""


class BaseModel:
    """BaseModel with identifying attributes of each instance"""
    def __init__(self, *args, **kwargs):
        """Initialize base objects with id, created_at and updated_at
        attributes
        Args:
            args (list): list of arguments
            kwargs (dict): dictionary of arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = uuid4().urn[9:]
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Saves the updated_at time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns each object to a dictionary"""
        new_key = self.__dict__
        new_key['__class__'] = type(self).__name__
        new_key['created_at'] = new_key['created_at'].isoformat()
        new_key['updated_at'] = new_key['updated_at'].isoformat()
        return new_key

    def __str__(self):
        """Prints out a string representation of an object"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)