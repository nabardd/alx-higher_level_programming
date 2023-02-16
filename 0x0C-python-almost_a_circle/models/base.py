#!/usr/bin/python3
import json
import os

"""Base class"""

class Base:
    
    """
    This class serves as the base for all classes
    in this project
    """
    
    def __init__(self, id=None):
        self.__nb_objects = 0

        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON representation of list_dictionaries

        Args:
            list_dictionaries (int): list of dictionaries
        """

        if list_dictionaries is None:
            list_dictionaries = []
        elif not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        
        for dictionary in list_dictionaries:
            if not isinstance(dictionary, dict):
                raise TypeError("list_dictionaries must be dictionaries")
        
        return json.dumps(list_dictionaries)
        
    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
            json_string (str): string representing a list of dictionaries
        """
        if json_string is None:
            return ([])
        else:
            if isinstance(json_string, str):
                return json.loads(json_string)
            raise TypeError("json_string must be a string")
        
    def save_to_file(cls, list_objs):
        """
        Writtes a JSON representation of list_objs to a file

        Args:
            list_objs: a list of instances who inherits of Base
        """
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
                file.write("[]")
        else:
            json_rep = cls.to_json_string(list_objs)

            with open("f{cls.__name__}.json", "w") as file:
                file.write(json_rep)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filepath = f"{cls.__name__}.json"

        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                f = file.read()
                list_dicts = cls.from_json_string(f)
                result = [cls.create(**d) for d in list_dicts]
            return result
        else:
            return ("[]")