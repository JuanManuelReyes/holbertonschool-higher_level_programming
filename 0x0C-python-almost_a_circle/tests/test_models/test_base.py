#!/usr/bin/python3
"""asd asd asd"""

import unittest
import json
import os

from models import base
from models import rectangle

Base = base.Base
Rectangle = rectangle.Rectangle

class TestBase(unittest.TestCase):
    """asd asd asd"""

    def test_id(self):
        """asd asd asd"""
        self.assertTrue(Base(666), self.id == 666)
        self.assertTrue(Base(15), self.id == 15)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(-6), self.id == -6)

    def test_args(self):
        """asd asd asd"""
        with self.assertRaises(TypeError):
            Base(10, 10)

    def test_to_json_string(self):
        """asd asd asd"""
        ob1 = {"id": 0, "width": 2, "height": 2, "x": 3, "y": 3}
        ob2 = {"id": 1, "width": 5, "height": 5, "x": 8, "y": 8}
        _str = Base.to_json_string([ob1, ob2])
        self.assertTrue(type(ob1) == dict)
        self.assertTrue(type(_str) == str)
        self.assertTrue(_str,
                        [{"id": 0, "width": 2, "height": 2, "x": 3, "y": 3},
                         {"id": 1, "width": 5, "height": 5, "x": 8, "y": 8}])

    def test_to_json_string_none(self):
        """asd asd asd"""
        ob2 = None
        _str1 = Base.to_json_string([ob2])
        self.assertTrue(type(_str1) == str)
        self.assertTrue(_str1, "[]")

    def test_to_json_string_empty(self):
        """asd asd asd"""
        ob3 = dict()
        _str2 = Base.to_json_string([ob3])
        self.assertTrue(len(ob3) == 0)
        self.assertTrue(type(_str2) == str)
        self.assertTrue(_str2, "[]")

    def test_from_json_string_none(self):
        """asd asd asd"""
        ob4 = None
        _str3 = Base.from_json_string(ob4)
        self.assertTrue(type(_str3) == list)
        self.assertTrue(_str3 == [])

    def test_from_json_string_empty(self):
        """asd asd asd"""
        ob5 = ""
        _str4 = Base.from_json_string(sob53)
        self.assertTrue(type(_str4) == list)
        self.assertTrue(_str4 == [])

    def test_create(self):
        """asd asd asd"""
        rec = Rectangle(6, 3, 1, 2, 66)
        rec_dic = rec.to_dictionary()
        rec2 = Rectangle.create(**rec_dic)
        self.assertEqual(str(rec), '[Rectangle] (66) 1/2 - 6/3')
        self.assertEqual(str(rec2), '[Rectangle] (66) 1/2 - 6/3')
        self.assertIsNot(rec, rec2)

    def test_save_to_file(self):
        """asd asd asd"""
        rec = Rectangle(10, 7, 2, 8, 99)
        rec2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([rec, rec2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([rec.to_dictionary(), rec2.to_dictionary()]),
                file.read())

    def test_save_to_file_none(self):
        """asd asd asd"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_empty_none_to_file(self):
        """asd asd asd"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_load_from_file(self):
        """asd asd asd"""
        rec = Rectangle(1, 5, 2, 6, 33)
        rec2 = Rectangle(4, 3, 2, 2, 58)
        Rectangle.save_to_file([rec, rec2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for i, x in enumerate(recs):
            if i == 0:
                self.assertEqual(str(x), '[Rectangle] (33) 2/6 - 1/5')
            if i == 1:
                self.assertEqual(str(x), '[Rectangle] (58) 2/2 - 4/3')

    def test_load_from_file_none(self):
        """asd asd asd"""
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_file_empty(self):
        """asd asd asd"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)