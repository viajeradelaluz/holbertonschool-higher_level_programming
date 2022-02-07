#!usr/bin/python3
""" Module for Unittest for Square class
    """

import unittest
from io import StringIO
from unittest.mock import patch
from models import square
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Testing the Square class
        """

    def setUp(self):
        """ Method to prepare each single test """
        Base._Base__nb_objects = 0

    def test_module_documentation(self):
        """ Test if base module is documented
            """
        self.assertTrue(Square.__doc__)

    def test_class_documentation(self):
        """ Test if Square class is documented
            """
        self.assertTrue(Square.__doc__)

    def test_square_simple_instance(self):
        """ Test a Square instance only with size
            """
        r = Square(13)
        self.assertEqual(r.size, 13)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_square_full_instance(self):
        """ Test a Square instance with full parameters
            """
        r = Square(8, 3, 1, 30)
        self.assertEqual(r.size, 8)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 30)

    def test_square_instance_few_arguments(self):
        """ Test a Square instance without any argument
            """
        with self.assertRaises(TypeError):
            r = Square()

    def test_private_attr_access(self):
        """ Test private attributes can't be accessed
            """
        with self.assertRaises(AttributeError):
            print(Square.__size)
            print(Square.size)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_square_instance_update_id(self):
        """ Test a Square instance updating the value for id
            """
        r = Square(18)
        r.id = 91
        self.assertEqual(r.id, 91)

    def test_square_instance_wrong_type_size(self):
        """ Test a Square instance with wrong data type
            """
        with self.assertRaises(TypeError):
            r = Square('10')
        with self.assertRaises(TypeError):
            r = Square(3.4)
        with self.assertRaises(TypeError):
            r = Square((10, 2))
        with self.assertRaises(TypeError):
            r = Square([10, 2])

    def test_square_instance_zero_size(self):
        """ Test a Square instance with zero number at size
            """
        with self.assertRaises(ValueError):
            r = Square(0)

    def test_square_instance_negative_size(self):
        """ Test a Square instance with negative number at size
            """
        with self.assertRaises(ValueError):
            r = Square(-8)

    def test_square_instance_update_size(self):
        """ Test a Square instance updating values for size
            """
        r = Square(4)
        r.size = 15
        self.assertEqual(r.size, 15)

    def test_square_instance_zero_x_y(self):
        """ Test a Square instance wit zero number at x or y
            """
        r = Square(5, 0, 2)
        self.assertEqual(r.x, 0)
        r = Square(9, 4, 0)
        self.assertEqual(r.y, 0)

    def test_square_instance_wrong_type_x_y(self):
        """ Test a Square instance with wrong x, y parameters
            """
        with self.assertRaises(TypeError):
            r = Square(8, 3.5, 7.8)
        with self.assertRaises(TypeError):
            r = Square(15, (4, 8))
        with self.assertRaises(TypeError):
            r = Square(15, '7', 6)

    def test_square_instance_negative_x_y(self):
        """ Test a Square instance with negative at x or y
            """
        with self.assertRaises(ValueError):
            r = Square(5, -4, 3)
        with self.assertRaises(ValueError):
            r = Square(5, 2, -7)

    def test_square_area_method(self):
        """ Test the area method of a Square
            """
        r = Square(7)
        self.assertEqual(r.area(), 49)

    def test_square_area_method_update(self):
        """ Test if the area method is updatable
            """
        r = Square(8)
        self.assertEqual(r.size, 8)
        self.assertEqual(r.area(), 64)

        r.area = 17
        self.assertEqual(r.size, 8)
        self.assertEqual(r.area, 17)

    def test_square_area_method_with_arguments(self):
        """ Test if the area method receives arguments
            """
        r = Square(9, 7)
        with self.assertRaises(TypeError):
            r.area(5)

    def test_square_display_width_height(self):
        """ Test a Square representation of size in stdout
            """
        r = Square(4)
        expected = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_square_display_widht_height_x_y(self):
        """ Test a Square representation size/x/y in stdout
            """
        r = Square(2, 1, 2)
        expected = "\n\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_square_standar_str_print(self):
        """ Test a standar output when print() is called
            """
        r = Square(6, 2, 1, 30)
        expected = "[Square] (30) 2/1 - 6\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            print(r)
            self.assertEqual(printed.getvalue(), expected)

    def test_square_str_return(self):
        """ Test the __str__ return of a Square instance
            """
        r = Square(7)
        expected = "[Square] (1) 0/0 - 7"
        self.assertEqual(r.__str__(), expected)

    def test_square_update_method(self):
        """ Test the update method of a Square instance
            """
        r = Square(8, 2, 2, 15)
        print_r = "[Square] (15) 2/2 - 8"
        self.assertEqual(r.__str__(), print_r)

        r.update(10, 9, 1, 1)
        print_r = "[Square] (10) 1/1 - 9"
        self.assertEqual(r.__str__(), print_r)

    def test_square_update_empty_arguments(self):
        """ Test the update method without any arguments
            """
        r = Square(9)
        self.assertFalse(r.update())

    def test_square_update_by_kwargs(self):
        """ Test update method by dictionary keys
            """
        r = Square(18)
        r.update(id=25, size=14)
        self.assertEqual(r.id, 25)
        self.assertEqual(r.size, 14)

    def test_update_mixing_args_kwargs(self):
        """ Test update method mixing args and kwargs
            """
        r = Square(32)
        self.assertFalse(r.update(10, 22, x=2, y=5))

    def test_square_to_dictionary_method(self):
        """ Test to_dictionary method for a Square instance
            """
        r = Square(15, 1, 2, 10)
        r_dict = r.to_dictionary()
        self.assertIsInstance(r_dict, dict)

    def test_square_to_dictionary_arguments(self):
        """ Test if to_dictionary method receives arguments
            """
        r = Square(8)
        with self.assertRaises(TypeError):
            r_dict = r.to_dictionary(size=9)
