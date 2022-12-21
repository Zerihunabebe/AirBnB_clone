#!/usr/bin/python3

""" Module File Storage """

import json
from models.base_model import BaseModel
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    """ This class serializes instances to a JSON file and"""
    """ deserializes JSON file to instances """
    """__file_path: string - path to the JSON file (ex: file.json)"""
    """__objects: dictionary - empty but will store all objects by"""
    """ <class name>.id ex: BaseModel.12121212"""

    __file_path = "object_contents.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_objects = {}
        for key in self.__objects:
            new_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(new_objects))

    def reload(self):
        """deserializes the JSON file to __objects, only if the JSON file"""
        """__file_path exists ; otherwise, do nothing. If the file doesnt"""
        """exist, no exception should be raised"""
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    new_objects = json.load(file)
                for key, value in new_objects.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
            except:
                pass
