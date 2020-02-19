#!/usr/bin/python3
"""
FileStorage Module

"""
import json


class FileStorage:
    """class that serializes and deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        FileStorage.__objects.update({"{}.{}".format(
            obj.__class__.__name__, obj.id): obj})

    def save(self):
        """serializes __objects to the JSON file"""
        json_dict = {}

        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(json_dict, my_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                from models.base_model import BaseModel
                from models.user import User
                dict_ = json.load(file)
                for key, value in dict_.items():
                    my_class = value["__class__"]
                    new_obj = (eval(my_class)(**value))
                    FileStorage.__objects.update({(key): new_obj})
        except IOError:
            pass
