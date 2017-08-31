#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assingment 1 part 2 - A simple class"""

class BOOK(object):
    """Object that represents a book."""

    def __init__(self, author, title):
        """Constructor for BOOK class.
        Args:
            author (str): name of person who wrote book
            title (str): title of a book

        Attributes:
            author (str): name of person who wrote book
            title (str): title of a book
        """
        self.author = author
        self.title = title


class OFMICEANDMEN(BOOK):
    """Object that stores data about a book."""

    author = "John Stienbeck"
    title = "Of Mice and Men"


class TOKILLAMOCKINGBIRD(BOOK):
    """Object that stores data about a book."""

    author = "Harper Lee"
    title = "To Kill a Mocking Bird"


def display(book_class):
    """funstion that displays the data about a book.

    Args:
        book_class (class): class to display info for.

    Returns:
        str : title of book written by author of book

    Examples:
        >>> display(TOKILLAMOCKINGBIRD)
        To Kill a Mocking Bird written by Harper Lee
    """

    print book_class.title + ' written by ' + book_class.author
