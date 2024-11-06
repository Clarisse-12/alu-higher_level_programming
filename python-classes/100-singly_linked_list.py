#!/usr/bin/python3
"""
This module defines a singly linked list data structure.

It includes the `Node` class for individual elements and the
`SinglyLinkedList` class for managing a sorted singly linked list.
"""


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data for the node. Must be an integer.
            next_node (Node or None): The next node in the list, or None if it is the last node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, DataValue):
        """
        Set the data for the node.

        Args:
            DataValue (int): The new data value.

        Raises:
            TypeError: If DataValue is not an integer.
        """
        if not isinstance(DataValue, int):
            raise TypeError("data must be an integer")
        self.__data = DataValue

    @property
    def next_node(self):
        """
        Retrieve the next node in the list.

        Returns:
            Node or None: The next node, or None if this is the last node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, NodeValue):
        """
        Set the next node in the list.

        Args:
            NodeValue (Node or None): The node to link as the next node.

        Raises:
            TypeError: If NodeValue is not a Node instance or None.
        """
        if NodeValue is not None and not isinstance(NodeValue, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = NodeValue


class SinglyLinkedList:
    """
    A class to represent a sorted singly linked list.

    The list maintains nodes in ascending order.
    """

    def __init__(self):
        """
        Initialize an empty SinglyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, DataValue):
        """
        Insert a new Node with the specified value in sorted order.

        Args:
            DataValue (int): The value to insert.
        """
        new_node = Node(DataValue)
        if self.__head is None:
            self.__head = new_node
            return
        if DataValue < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while DataValue >= current.data:
            previous = current
            if current.next_node:
                current = current.next_node
            else:
                current.next_node = new_node
                return
        previous.next_node = new_node
        new_node.next_node = current

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: A newline-separated string of each node's data.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")

