#!usr/bin/python3
""" Module with Unittest for Base class
    """
import unittest
import pep8
import inspect
import json

from models import base
from models.square import Square
from models.rectangle import Rectangle
from os.path import exists as file_exists

Base = base.Base


class TestBase(unittest.TestCase):
    """ Testing the Base class
        """

    def setUp(self):
        """ Method to prepare each single test """
        Base._Base__nb_objects = 0

    def test_module_documentation(self):
        """ Test if base module is documented
            """
        self.assertTrue(base.__doc__)

    def test_class_documentation(self):
        """ Test if Base class is documented
            """
        self.assertTrue(Base.__doc__)

    def test_methods_documentation(self):
        """ Test if all Base methods are documented
            """
        methods = inspect.getmembers(Base)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8
            """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_basic_base_assigment(self):
        """ Create a basic Base instance
            """
        b1 = Base()
        b2 = Base()
        b3 = Base(15)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 15)

    def test_base_assigment_no_id(self):
        """  Create multiple basic Base instances
            """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_assigment_id(self):
        """  Create a Base instance with id
            """
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_private_attr_access(self):
        """ Test private attributes can't be accesse
            """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_mix_base_assigment_id(self):
        """ Create multiple Base instances with and without id
            """
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 2)

    def test_base_assigment_more_arguments(self):
        """ Test Base instance assigment with more arguments
            """
        with self.assertRaises(TypeError):
            b = Base(10, 20)

    def test_base_string_id(self):
        """ Test for string assigment as id
            """
        b = Base('15')
        self.assertEqual(b.id, '15')

    def test_to_json_string(self):
        """ Check if to_json_string method return a str
            """
        r = Square(15, 7, 6, 30)
        r_dict = r.to_dictionary()
        json_str = Base.to_json_string([r_dict])

        self.assertIsInstance(json_str, str)
        dict_r = json.loads(json_str)
        self.assertEqual(dict_r, [r_dict])

    def test_save_to_file_no_arguments(self):
        """ Check the save_to_file method without arguments"""
        r = Square(8)
        with self.assertRaises(TypeError):
            r.save_to_file()

    def test_save_to_file_more_arguments(self):
        """ Check the save_to_file method with more arguments
            """
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r.save_to_file([r], [])

    def test_from_json_string(self):
        """ Test the normal use for from_json_string method
            """
        dict_list = [
            {'id': 10, 'size': 15, 'x': 1, 'y': 2},
            {'id': 7, 'size': 14, 'x': 2, 'y': 1, }
        ]
        json_str = Base.to_json_string(dict_list)
        json_dict_list = Base.from_json_string(json_str)

        self.assertIsInstance(json_dict_list, list)
        self.assertIsInstance(json_dict_list[0], dict)
        self.assertIsInstance(json_dict_list[1], dict)

    def test_from_json_string_none_empty(self):
        """ Test from_json_string method for None or empty argument
            """
        json_dict_list = Base.from_json_string(None)
        self.assertIsInstance(json_dict_list, list)

        json_dict_list = Base.from_json_string([])
        self.assertIsInstance(json_dict_list, list)

        with self.assertRaises(TypeError):
            json_dict_list = Base.from_json_string()

    def test_from_json_string_wrong_type(self):
        """ Test for passing wrong data type to from_json_string method
            """
        with self.assertRaises(TypeError):
            json_dict_list = Base.from_json_string([("r1"), ("r2")])

    def test_create(self):
        """ Test normal use of the create method
            """
        r1 = Square(8, 2, 2)
        r1_dict = r1.to_dictionary()
        r2 = Square.create(**r1_dict)
        print_r2 = "[Square] (1) 2/2 - 8"

        self.assertIsInstance(r2, Square)
        self.assertEqual(r2.__str__(), print_r2)

    def test_create_without_dict(self):
        """ Check the create method passing a square
            """
        r1 = Square(9)
        with self.assertRaises(TypeError):
            r2 = Square.create(**r1)

    def test_create_more_arguments(self):
        """ """
        r1 = Square(15)
        r2 = Square(25)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        with self.assertRaises(TypeError):
            r = Square.create(**r1_dict, **r2_dict)

    def test_load_from_file_reads_file(self):
        """ Check if load_from_file method reads the file
            """
        r1 = Square(4, 5, 9, 30)
        r2 = Square(7, 3, 8, 30)
        r_input = [r1, r2]
        Square.save_to_file(r_input)
        r_output = Square.load_from_file()

        self.assertIsInstance(r_output, list)
        self.assertFalse(len(r_output) == 0)

    def test_load_from_file_empty_file(self):
        """ Check if load_from_file method works without a file
            """
        list_instances = Square.load_from_file()

        self.assertIsInstance(list_instances, list)
        self.assertTrue(len(list_instances) == 0)
