#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""


import json


class Base:
    """Represents base of all classes created

    Private class attributes:
        __nb_objects(int): number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Represents a new base

        Args:
            id: identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
