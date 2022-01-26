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
