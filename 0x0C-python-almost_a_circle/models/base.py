#!/usr/bin/python3
"""My base package"""
import json
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to file."""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation."""
        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create instance with attributes set."""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='UTF-8') as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV string representation of list_objs to file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'a', encoding='UTF-8') as f:  # Open in append mode
            writer = csv.writer(f)
            if list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(["id", "width", "height", "x", "y"])
                    for obj in list_objs:
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                else:
                    writer.writerow(["id", "size", "x", "y"])
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])
