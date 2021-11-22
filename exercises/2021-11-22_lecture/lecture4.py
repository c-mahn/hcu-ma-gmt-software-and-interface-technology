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

# Task 5:
# What do the // and % operators do? How are they different from each other?

# Task 6:
# What is the difference between = and == in Python?

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
# import string as st
# import random as r
# import re

# Functions
# -----------------------------------------------------------------------------


# Task 0
ages = lambda list_of_birthyears: [2021-x for x in list_of_birthyears]


# Task 1
def overlapping(list1, list2):
    """
    Compares 2 lists and returns elements contained in both lists back.

    Args:
        list1 ([list]): [a list with elements]
        list2 ([list]): [a list with elements]
    """
    result = []
    for i in list1:
        for j in list2:
            if(i == j):
                result.append(i)
    return(result)


# Task 2
def tree_print(list1):
    """
    Prints a list and removes one list element each iteration.

    Args:
        list1 ([list]): [a list with elements]
    """
    result = []
    while(list1 != []):
        print(list1)
        result.append(list(list1))
        list1.pop(-1)
    return(result)


# Task 3
def dot_replace(string1):
    """
    This function replaces dots with spaces in a string. If the string ends
    with a dot, it will be preserved.

    Args:
        string1 ([string]): [a string with dots]
    """
    result = ""
    for i, e in enumerate(string1):
        if(e == "."):
            if(i == len(string1)-1):
                result = f"{result}{e}"
            else:
                result = f"{result} "
        else:
            result = f"{result}{e}"
    return(result)


# Task 10
def alternating(list1):
    """
    This function prints every second element in a list.

    Args:
        list1 ([list]): [a list with elements]
    """
    result = []
    for i, e in enumerate(list1):
        if(i%2 == 0):
            print(e)
            result.append(e)
    return(result)


# Task 11
def multiples(int1, int2):
    """
    This function generates a list with multiples of an integer, until the
    limit is reached.

    Args:
        int1 ([int]): [multiples of this integer]
        int2 ([int]): [limit, where the algorithim will stop]
    """
    i = int1
    result = []
    while(i <= int2):
        result.append(i)
        i += int1
    return(result)


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    
    # Answer for task 7:
    string1 = "Hamburg"
    print(string1[0:4])

    # Answer for task 8:
    string1 = "Silverstone"
    print(string1[6:11])

    # Answer for task 9:
    string1 = "runcanrun"
    print(string1[3:6])
