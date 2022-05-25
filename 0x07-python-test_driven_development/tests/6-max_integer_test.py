#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
        """asd asd asd"""

        def test_one_elment_cases(self):
                """asd asd asd"""
                self.assertEqual(max_integer([1]), 1)
                self.assertEqual(max_integer([666]), 666)
                self.assertEqual(max_integer([4141]), 4141)
                self.assertEqual(max_integer([123, -456, 789]), 789)
                self.assertEqual(max_integer([1122, 3366]), 3366)
                self.assertEqual(max_integer([[1, 2], [-3, -4], [5, 6]]), [5, 6])
                self.assertEqual(max_integer([[11, 22], [-1, -2], [2, 4]]), [11, 22])
                self.assertEqual(max_integer(['a', 'e', 'i', 'o', 'u']), 'u')
                self.assertEqual(max_integer("aeiou"), 'u')
                self.assertEqual(max_integer("59898721550"), '9')
                self.assertEqual(max_integer(["The", "Little", "Reyes"]), "Little")
                self.assertIsNone(max_integer([]), None)
                self.assertIsNone(max_integer(), None)
                self.assertIsNone(max_integer([None]), None)
                with self.assertRaises(TypeError):
                        max_integer({6, 6, 6})
                with self.assertRaises(TypeError):
                        max_integer(666)

        if __name__ == "__main__":
                unittest.main()
