#!/usr/bin/python3
"""asd asd asd"""

import json
import csv
import os


class Base():
    """asd asd asd"""

    __nb_objects = 0

    def __init__(self, id=None):
        """asd asd asd"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """asd asd asd"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """asd asd asd"""

        filename = cls.__name__ + ".json"
        list = []

        if list_objs is not None:
            for i in list_objs:
                list.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """asd asd asd"""

        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """asd asd asd"""

        if cls.__name__ is "Square":
            dummy = cls(1)
        elif cls.__name__ is "Rectangle":
            dummy = cls(1, 1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """asd asd asd"""

        filename = cls.__name__ + ".json"
        list = []

        try:
            with open(filename, mode="r") as f:
                raw_json = f.read()

            dic_list = cls.from_json_string(raw_json)

            for i in dic_list:
                list.append(cls.create(**i))

        except Exception:
            pass

        return list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """asd asd asd"""

        my_list_objs = [x.to_dictionary() for x in list_objs]

        filename = cls.__name__ + ".csv"

        if(cls.__name__ == "Rectangle"):
            columns = ["id", "width", "height", "x", "y"]

        if(cls.__name__ == "Square"):
            columns = ["id", "size", "x", "y"]

        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=columns)

        writer.writeheader()

        for dict in list_objs:
            writer.writerow(dict.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """asd asd asd"""

        list = []

        filename = cls.__name__ + ".csv"

        if not os.path.isfile(filename):
            return (list)

        with open(filename) as f:
            reader = csv.DictReader(f)

            for row in reader:
                row = {key: int(row[key]) for key in row.keys()}
                list.append(cls.create(**row))

        return(list)