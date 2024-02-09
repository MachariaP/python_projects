#!/usr/bin/python3

from datetime import datetime
import uuid

class BaseModel:
    """Base class for all models in the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        if kwargs.get('id') is None:  # Check if 'id' is not provided
            self.id = str(uuid.uuid4())  # Generate a new UUID
        else:
            self.id = kwargs['id']  # Use the provided 'id'

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__' and key != 'id':  # Exclude 'id' from kwargs
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(
                class_name, self.id, self.to_dict())

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
