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
        """ Define the size attribute
            """
        return self.width

    @size.setter
    def size(self, value):
        """ Define size behavior
            """
        self.width = value
        self.height = value

    def __str__(self):
        """ Set the standar values for the print function
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
        d = {
            'id': self.id, 'size': self.size,
            'x': self.x, 'y': self.y
        }

        return d
