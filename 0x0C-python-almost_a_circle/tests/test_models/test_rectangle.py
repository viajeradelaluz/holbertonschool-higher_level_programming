#!usr/bin/python3
""" Module for Unittest for Rectangle class
    """
import unittest
import inspect
import os

from io import StringIO
from unittest.mock import patch
from models import rectangle
from models.base import Base

Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """ Testing the Rectangle class
        """

    def setUp(self):
        """ Method to prepare each single test """
        Base._Base__nb_objects = 0

    def test_module_documentation(self):
        """ Test if rectangle module is documented
            """
        self.assertTrue(rectangle.__doc__)

    def test_class_documentation(self):
        """ Test if Rectangle class is documented
            """
        self.assertTrue(Rectangle.__doc__)

    def test_methods_documentation(self):
        """ Test if all Rectangle methods are documented
            """
        methods = inspect.getmembers(Rectangle)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_rectangle_simple_instance(self):
        """ Test a rectangle instance only with width and height
            """
        r = Rectangle(13, 6)
        self.assertIsInstance(r, Rectangle)
        self.assertTrue(issubclass(type(r), Base))
        self.assertEqual(r.width, 13)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rectangle_full_instance(self):
        """ Test a rectangle instance with full parameters
            """
        r = Rectangle(8, 14, 3, 1, 30)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 14)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 30)

    def test_rectangle_instance_few_arguments(self):
        """ Test a rectangle instance with only one argument
            """
        with self.assertRaises(TypeError):
            r = Rectangle(6)

    def test_private_attr_access(self):
        """ Test private attributes can't be accessed
            """
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_rectangle_instance_update_id(self):
        """ Test a rectangle instance updating the value for id
            """
        r = Rectangle(2, 10)
        r.id = 91
        self.assertEqual(r.id, 91)

    def test_rectangle_instance_wrong_type_width_height(self):
        """ Test a rectangle instance with a wrong data type
            """
        with self.assertRaises(TypeError):
            r = Rectangle('10', 2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, '2')

    def test_rectangle_instance_zero_width_height(self):
        """ Test a rectangle instance with zero number at width or height
            """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 7)
        with self.assertRaises(ValueError):
            r = Rectangle(18, 0)

    def test_rectangle_instance_negative_width_height(self):
        """ Test a rectangle instance with negative at width or height
            """
        with self.assertRaises(ValueError):
            r = Rectangle(-8, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(3, -8)

    def test_rectangle_instance_update_width_height(self):
        """ Test a rectangle instance updating values for width or height
            """
        r = Rectangle(2, 10)
        r.width = 15
        r.height = 22
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 22)

    def test_rectangle_instance_zero_x_y(self):
        """ Test a rectangle instance wit zero number at x or y
            """
        r = Rectangle(5, 8, 0, 2)
        self.assertEqual(r.x, 0)
        r = Rectangle(9, 2, 4, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_instance_wrong_type_x_y(self):
        """ Test a rectangle instance with wrong x, y parameters
            """
        with self.assertRaises(TypeError):
            r = Rectangle(15, 4, '7', 6)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, '4')

    def test_rectangle_instance_negative_x_y(self):
        """ Test a rectangle instance with negative at x or y
            """
        with self.assertRaises(ValueError):
            r = Rectangle(5, 3, -4, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 3, 2, -7)

    def test_rectangle_area_method(self):
        """ Test the area method of a rectangle
            """
        r = Rectangle(7, 9)
        self.assertEqual(r.area(), 63)

    def test_rectangle_area_method_update(self):
        """ Test if the area method is updatable
            """
        r = Rectangle(8, 4)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.area(), 32)

        r.area = 17
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.area, 17)

    def test_rectangle_area_method_with_arguments(self):
        """ Test if the area method receives arguments
            """
        r = Rectangle(9, 7)
        with self.assertRaises(TypeError):
            r.area(5)

    def test_rectangle_display_width_height(self):
        """ Test a Rectangle representation widht/height in stdout
            """
        r = Rectangle(3, 4)
        expected = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_rectangle_display_widht_height_x_y(self):
        """ Test a Rectangle representation widht/height/x/y in stdout
            """
        r = Rectangle(2, 4, 1, 2)
        expected = "\n\n ##\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_rectangle_standar_str_print(self):
        """ Test a standar output when print() is called
            """
        r = Rectangle(6, 8, 2, 1, 30)
        expected = "[Rectangle] (30) 2/1 - 6/8\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            print(r)
            self.assertEqual(printed.getvalue(), expected)

    def test_rectangle_str_return(self):
        """ Test the __str__ return of a Rectangle instance
            """
        r = Rectangle(7, 9)
        expected = "[Rectangle] (1) 0/0 - 7/9"
        self.assertEqual(r.__str__(), expected)

    def test_rectangle_update_method(self):
        """ Test the update method of a Rectangle instance
            """
        r = Rectangle(8, 3, 2, 2, 15)
        print_r = "[Rectangle] (15) 2/2 - 8/3"
        self.assertEqual(r.__str__(), print_r)

        r.update(10, 4, 9, 1, 1)
        print_r = "[Rectangle] (10) 1/1 - 4/9"
        self.assertEqual(r.__str__(), print_r)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_rectangle_update_empty_arguments(self):
        """ Test the update method without any arguments
            """
        r = Rectangle(9, 6)
        self.assertFalse(r.update())

    def test_rectangle_update_by_kwargs(self):
        """ Test update method by dictionary keys
            """
        r = Rectangle(25, 3)
        r.update(id=25, width=18, height=4, x=2, y=2)
        self.assertEqual(r.id, 25)
        self.assertEqual(r.width, 18)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_update_mixing_args_kwargs(self):
        """ Test update method mixing args and kwargs
            """
        r = Rectangle(56, 32)
        self.assertFalse(r.update(10, 22, 32, x=2, y=5))

    def test_rectangle_to_dictionary_method(self):
        """ Test to_dictionary method for a Rectangle instance
            """
        r = Rectangle(15, 9, 1, 2, 10)
        r_dict = r.to_dictionary()
        dict_r = {'x': 1, 'y': 2, 'id': 10, 'height': 9, 'width': 15}
        self.assertIsInstance(r_dict, dict)
        self.assertDictEqual(r_dict, dict_r)

    def test_rectangle_to_dictionary_arguments(self):
        """ Test if to_dictionary method receives arguments
            """
        r = Rectangle(8, 24)
        with self.assertRaises(TypeError):
            r_dict = r.to_dictionary(width=6, height=9)

    def test_save_to_file(self):
        """ Test normal use of the save_to_file method
            """
        r1 = Rectangle(8, 16, 2, 2, 15)
        r2 = Rectangle(7, 16, 3, 3, 15)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        """ Check the save_to_file method with None
            """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty(self):
        """ Check the save_to_file method with empty argument
            """
        r_list = []
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file(r_list)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual("[]", f.read())
