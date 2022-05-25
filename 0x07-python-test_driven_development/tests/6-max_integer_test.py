#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """asd asd asd"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, -1, -2]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([-1, -2, -64, -34]), -1)
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([1, 15, 4]), 15)
    
    if __name__ == "__main__":
        unittest.main()
