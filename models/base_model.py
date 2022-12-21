import uuid
from datetime import datetime
import models


class BaseModel:

    """class containing Public instance attributes"""

    def __init__(self, *args, **kwargs):

        """generate unique id converted to string and format datetime"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                        continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """save class data into a file to use it later"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a distionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
