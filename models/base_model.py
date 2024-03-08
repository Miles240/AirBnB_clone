#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_class = self.__dict__
        dict_class["__class__"] = self.__class__.__name__
        return dict_class

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
