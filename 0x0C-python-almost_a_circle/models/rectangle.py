#!/usr/bin/python3
"""Rectangle class
    """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Builder of Rectagle class
            """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width of the Rectangle
            """
        return self.__width

    @width.setter
    def width(self, value):
        """Width methods
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height of the Rectangle
            """
        return self.__height

    @height.setter
    def height(self, value):
        """Height methods
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x of the Rectangle
            """
        return self.__x

    @x.setter
    def x(self, value):
        """x methods
            """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y of the Rectangle
            """
        return self.__y

    @y.setter
    def y(self, value):
        """y methods
            """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle
            """
        return self.__width * self.__height

    def display(self):
        """ Print stdout the Rectangle
            """
        to_print = self.__y * "\n"
        for i in range(self.__height):
            to_print += " " * self.__x
            to_print += "#" * self.__width + "\n"

        print(to_print, end="")

    def __str__(self):
        """ Set the print function
            """
        s_id = "({}) ".format(self.id)
        s_xy = "{}/{} - ".format(self.__x, self.__y)
        s_wh = "{}/{}".format(self.__width, self.__height)

        return "[Rectangle] " + s_id + s_xy + s_wh

    def update(self, *args, **kwargs):
        """ Update the values of the attributes
            """
        if args is not None and len(args) > 0:
            attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary representation
            """
        d = {}
        d.update(id=self.id, width=self.__width,
                 height=self.__height, x=self.__x, y=self.__y)
        return d
