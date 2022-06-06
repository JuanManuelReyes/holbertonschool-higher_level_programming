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

        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            for object in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([object.id, object.width, object.height, object.x, object.y])

                if cls.__name__ == "Square":
                    writer.writerow([object.id, object.size, object.x, object.y])

    @classmethod
    def load_from_file_csv(cls):
        """asd asd asd"""

        list = []

        filename = cls.__name__ + ".csv"

        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)

            for row in reader:
                if cls.__name__ == "Rectangle":
                    dict = {"id": int(row[0]), "width": int(row[1]),
                           "height": int(row[2]), "x": int(row[3]),
                           "y": int(row[4])}

                if cls.__name__ == "Square":
                    dict = {"id": int(row[0]), "size": int(row[1]),
                           "x": int(row[2]), "y": int(row[3])}

                list.append(cls.create(**dict))

        return(list)
