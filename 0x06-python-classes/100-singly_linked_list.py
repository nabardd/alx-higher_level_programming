#!/usr/bin/python3
"""Implementing a singly linked list"""


class Node:
    """Node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Initializing Node for singly linked list.

        Args:
            data (int): data to be stored in the node
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer.")
        
        if isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")
        
    @property
    def data(self):
        """Retrieving the data"""

        return self.__data
    
    @data.setter
    def data(self, value):
        """
        Set data to value

        Args:
            value (int): value of data
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")
        
    @property
    def next_node(self):
        """Retrieving next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setting next node to value"""

        if isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """Implementation of singly linked list"""

    def __init__(self) -> None:
        """Initialization"""
        self.__head = None
    
    def sorted_insert(self, value):
        """
        method to insert into singly linked list

        Args:
            value (int): data to be stored into new node.
        """
