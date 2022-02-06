#!/usr/bin/python3
"""Square class
    """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Builder of the Square class
            """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Define the size
            """
        return self.__width

    @size.setter
    def size(self, value):
        """ Define size behavior
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """ Print a representation of a square
            """
        s_id = "({}) ".format(self.id)
        s_xy = "{}/{} - ".format(self.x, self.y)
        s_size = "{}".format(self.size)

        return "[Square] " + s_id + s_xy + s_size

    def update(self, *args, **kwargs):
        """ Update the attributes
            """
        if args is not None and len(args) > 0:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary representation
            """
        d = {}
        d.update(id=self.id, size=self.size,
                 x=self.x, y=self.y)
        return d
