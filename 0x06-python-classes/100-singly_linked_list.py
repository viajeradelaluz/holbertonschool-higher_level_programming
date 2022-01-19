#!/usr/bin/python3
""" Handles single linked list """


class Node:
    """ Defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        return str(self.__data)


class SinglyLinkedList:
    """ Defines a singly linked list """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)

        traverse = self.__head
        if traverse is None or traverse.data >= value:
            if traverse:
                new.next_node = traverse
            self.__head = new
            return

        while traverse.next_node:
            if traverse.next_node.data >= value:
                break
            traverse = traverse.next_node

        new.next_node = traverse.next_node
        traverse.next_node = new

    def __str__(self):
        to_print = ""
        traverse = self.__head

        while traverse:
            to_print += str(traverse)
            if traverse.next_node is not None:
                to_print += "\n"
                traverse = traverse.next_node

        return to_print
