# Lecture 4 - Tasks
# #############################################################################

# Task 0:
# You are given a list of different years. Create a list with the ages
# corresponding to the birth years in one line of code (no printing).


# Task1:
# You are given two lists. Check them for overlapping values (if some value is
# present in the other list as well). If so, create a new list with the values
# in both lists.


# Task2:
# Given a Python list, print the list, remove the last element and print the
# list again. Repeat the process until the list is empty without printing the
# empty list.


# Task 3:
# Given a string with a sentence, replace the dots in the sentence by empty
# spaces (“ “). Leave the dot at the end.


# Task4:
# How would you go about catching an import error the right way?

# Answer:
# When catching import errors, I would match every line in the file with a
# regular expression. If the current line doesn't match the importing criteria,
# it will be ignored and a warning will be made available for the user.


# Task 5:
# What do the // and % operators do? How are they different from each other?

# Answer:
# "//" is a floor division, where the number is rounded down to the next whole
# number. Example: 5//3 = 1
# "%" is the modulo-operator, which returns the remainder in a division-
# operation. Example: 5%3 = 2


# Task 6:
# What is the difference between = and == in Python?

# Answer:
# "=" assigns data to a variable, while "==" is an operator for checking, if
# something is equal.


# Task 7:
# Given a string “Hamburg“, slice the string and print out everything until „b“
# (b included).


# Task 8:
# Given a string “Silverstone“, slice the string so it prints out „stone“.


# Task 9:
# Given a string „runcanrun“, slice the string and print out „can“.


# Task 10:
# Given a list, print every second value of the list.


# Task 11:
# Write a function that takes two integer arguments and returns a list of the
# multiples of the first value. The function is supposed to run until the
# length of the list has reached the second value.


# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

# import math as m
from lecture4 import *
# import re
# import string as st


# Functions
# -----------------------------------------------------------------------------


def test_task_00_1():
    """
    Test for task 0.
    """
    assert(ages([2020, 1900, 1990, 1998]) == [1, 121, 31, 23])


def test_task_01_1():
    """
    Test for task 1.
    """
    assert(overlapping([1, 2, 3, 4, 5], [1, 3, 5, 7, 9]) == [1, 3, 5])


def test_task_01_2():
    """
    Test for task 1.
    """
    assert(overlapping([1, 2, 3, 4, 5], [6, 7, 8, 9, 0]) == [])


def test_task_02_1():
    """
    Test for task 2.
    """
    assert(tree_print([1, "a"]) == [[1, "a"], [1]])


def test_task_02_2():
    """
    Test for task 2.
    """
    assert(tree_print([1, 2, 3, 4, 5]) == [[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1, 2], [1]])


def test_task_03_1():
    """
    Test for task 3.
    """
    assert(dot_replace("This.is.a.sentence.") == "This is a sentence.")


def test_task_10_1():
    """
    Test for task 10.
    """
    assert(alternating([1, 2, 3, 4, 5, 6, 7]) == [1, 3, 5, 7])


def test_task_11_1():
    """
    Test for task 11.
    """
    assert(multiples(3, 20) == [3, 6, 9, 12, 15, 18])


def test_task_11_2():
    """
    Test for task 11.
    """
    assert(multiples(2, 8) == [2, 4, 6, 8])


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
