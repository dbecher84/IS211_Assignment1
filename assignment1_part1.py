#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment one Functions and Exceptions"""

class ListDivideException(Exception):
    """class that represents and exception"""
    pass

def listdivide(numbers, divide=2):
    """A function to test how many numbers are divisible by a nubmer.

    Args:
        numbers (list): a list of number to test
        divide (int): a number to divide the list by. default = 2

    Returns:
        results (list): a list containing how many number are evenly
                        divisible by the divide arg.

    Example:
       >>> listdivide([2,5,6])
       [2]
    """

    num_divisible = 0
    results = []
    for number in numbers:
        try:
            if int(divide) == 0:
                raise ListDivideException
        except ListDivideException:
            print "Cannot divide by zero"
            break
        if int(number) % int(divide) == 0:
            num_divisible += 1
    results.append(num_divisible)
    return results


TEST_ITEMS = ([1, 2, 3, 4, 5], [2, 4, 6, 8, 10],
              [[30, 54, 63, 98, 100], 10], [],
              [[1, 2, 3, 4, 5], 1])

def testlistdivide(num_list=TEST_ITEMS, dividefunc=listdivide):
    """a function to test the listdivide function.

    Arg:
        num_list (list): a list of test number to test listdivide.
                         default = TEST_ITEMS
        dividefunc (function): the function to be tested.
                               default = listdivide

    Retunrs:
        nothing is returned unless an error is detected.
    """

    for item in num_list:
        if len(item) == 2:
            dividefunc(item[0], item[1])
        else:
            dividefunc(item)
