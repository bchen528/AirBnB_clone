#!/usr/bin/python3
"""This is a class FileStorage"""
import json


class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        Returns:
            __object dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj (obj): object
        """
        FileStorage.__object[type(obj).__name__ + ".id"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        file_to_open = FileStorage.__file_path + "file.json"
        with open(file_to_open, mode="w", encoding="utf-8") as a_file:
            json.dump(FileStorage.__objects, a_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        file_to_open = FileStorage.__file_path + "file.json"
        a_dict = {}
        with open(file_to_open, "r") as a_file:
            a_dict = json.load(a_file)
        print(a_dict)
