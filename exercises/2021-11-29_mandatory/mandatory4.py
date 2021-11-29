# Mandatory exercise 4
# #############################################################################


# Task 01
# Translate the following formula into Python:
# The Square-Root of (s(s-a)(s-b)(s-c))


# Task 02
# Translate the following formula into Python:
# The Square-Root of (a²-(b²/4))


# Task 03
# Write a function that returns a given integer with reversed digits.


# Task 04
# Write a function that returns the average word length in a sentence. Remember
# to remove punctuation ,.:;!?- first.


# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

import math as m
# import string as st
# import random as r
# import os

# Functions
# -----------------------------------------------------------------------------


# Task 01
def compute_result_1(s, a, b, c):
    return(m.sqrt(s*(s-a)*(s-b)*(s-c)))


# Task 02
def compute_result_2(a,b):
    return(m.sqrt((a**2)-((b**2)/(4))))


# Task 03
def reverse(number):
    return(str(number)[::-1])


# Task 04
def avg_word_length(some_string):
    some_string = some_string.replace(",", " ")
    some_string = some_string.replace(".", " ")
    some_string = some_string.replace(":", " ")
    some_string = some_string.replace(";", " ")
    some_string = some_string.replace("!", " ")
    some_string = some_string.replace("?", " ")
    some_string = some_string.replace("-", " ")
    dividend = 0
    divisor = 0
    word_list = some_string.split(" ")
    for i in word_list:
        if(len(i) > 0):
            dividend += len(i)
            divisor += 1
    try:
        result = dividend / divisor
        return(result)
    except(ZeroDivisionError):
        return(0.0)


# Classes
# -----------------------------------------------------------------------------




# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
