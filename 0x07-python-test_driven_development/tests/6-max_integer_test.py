#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Edge cases for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([7, 25, 88, 56]), 88)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-125, -22, -30]), -22)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_zero_as_argument(self):
        self.assertEqual(max_integer([36, 0, 15]), 36)

    def test_only_zero(self):
        self.assertEqual(max_integer([0]), 0)

    def test_float_numbers(self):
        self.assertEqual(max_integer([2.2, 8.9, 18.25]), 18.25)

    def test_inside_operations(self):
        self.assertEqual(max_integer([2 + 15, 5 * 5, 125 / 2]), 62.5)

    def test_max_between_strings(self):
        self.assertEqual(max_integer(["one", "two", "three"]), "two")

    def test_string_as_argument(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_without_list(self):
        with self.assertRaises(TypeError):
            max_integer(29, 25, 18, 22)

    def test_max_int(self):
        # Test max integers when passed lists and digits
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 5, 9, 5]), 9)
        self.assertEqual(max_integer([9, 5]), 9)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-6, -9, -2, 0]), 0)
        self.assertEqual(max_integer([-6, -9, -2, -3]), -2)
        self.assertEqual(max_integer((2, 4)), 4)

    def test_max_string(self):
        self.assertEqual(max_integer(["5", "7", "9"]), "9")
        self.assertEqual(max_integer(["Hello", "Good", "Bye"]), "Hello")
        self.assertEqual(max_integer("5"), "5")
        self.assertEqual(max_integer("4567"), "7")
        self.assertEqual(max_integer("abcxyz"), "z")
        self.assertEqual(max_integer(["a", "b", "c", "d", "e", "y", "z"]), "z")
        self.assertEqual(max_integer(["abc", "y"]), "y")

    def test_list_floats(self):
        self.assertEqual(max_integer([[1, 2], [2, 3]]), [2, 3])
        self.assertEqual(max_integer([{1, 2}, {2}, {3, 4}]), {1, 2})
        self.assertEqual(max_integer([-6.1, -9.8, -2.5, -3.7]), -2.5)

    def test_None(self):
        # Test max integers when list is empty
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    def test_errors(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1, 5)
