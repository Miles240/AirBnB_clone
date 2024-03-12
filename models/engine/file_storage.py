#!/usr/bin/python3
"""Contains the FileStorage class"""

import json
import os.path



class FileStorage:
    """class for FileStorage"""

    def __init__(self):
        """Initialization of FileStorage instances
        Args:
                - __file_path: json file
                - __objects: dictionary representation an instance
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns all dictionary representations"""
        return self.__objects

    def new(self, obj):
        """create a new key/value pair object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize and store the JSON representation of instances"""
        # Load existing data from the file, if any
        existing_data = {}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                existing_data = json.load(file)
        
        # Append new data to the existing data
        for key, value in self.__objects.items():
            existing_data[key] = value.to_dict()

        # Write the combined data back to the file
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(existing_data, file)

    def reload(self):
        """Deserialize and load objects from the JSON file."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    # Split the key into class name and object ID
                    parts = key.split(".")
                    if len(parts) != 2:
                        # Skip this entry if key is not in the expected format
                        continue
                    class_name, obj_id = parts
                    # Check if the class name exists in the current namespace
                    if class_name not in globals():
                        print(f"Class '{class_name}' not found in current namespace.")
                        continue
                    # Retrieve the class from the global namespace
                    obj_class = globals()[class_name]
                    # Instantiate an object of the class using the serialized data
                    obj = obj_class(**value)
                    # Store the object in the '__objects' dictionary
                    self.__objects[key] = obj
