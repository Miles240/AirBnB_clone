#!/usr/bin/python3

"""Module for the filestorage class"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenities
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Representation of FileStorage class
    Args:
        __file_path(file location): the file to store the serialized json objects
        __objects(dict): python dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """deserialize and loads objects from the json file"""
        if os.path.isfile(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) > 0:
                with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                    data = json.load(file)
                    for key, value in data.items():
                        cls_name, obj_id = key.split(".")
                        cls_ = eval(cls_name)
                        obj = cls_(**value)
                        FileStorage.__objects[key] = obj
            else:
                return
