#!/usr/bin/python3
""" defines all common atributes/methods"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """class that defines all common attributes/methods for other classes:"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "updated_at" or key == "created_at":
                    n_value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, n_value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Print Method """
        msg = "[{}] ({}) {}".format(
            BaseModel.__name__, self.id, self.__dict__)
        return msg

    def save(self):
        """updates the updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
