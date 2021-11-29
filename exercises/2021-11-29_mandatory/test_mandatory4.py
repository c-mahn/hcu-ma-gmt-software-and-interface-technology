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

# import math as m
from mandatory4 import *
# import re
# import string as st


# Functions
# -----------------------------------------------------------------------------


def test_task_01_a():
    assert(compute_result_1(25,2,3,4) == 515.412456194066)


def test_task_01_b():
    assert(compute_result_1(1,1,1,1) == 0.0)


def test_task_01_c():
    assert(compute_result_1(-1,-1,-1,-1) == 0.0)


def test_task_02_a():
    assert(compute_result_2(10, 5) == 9.682458365518542)


def test_task_02_b():
    assert(compute_result_2(25, 25) == 21.650635094610966)


def test_task_02_c():
    assert(compute_result_2(2, -2) == 1.7320508075688772)


def test_task_03_a():
    assert(reverse(123) == "321")


def test_task_03_b():
    assert(reverse(700) == "007")


def test_task_04_a():
    assert(avg_word_length("This ;: is a sentence :;;") == 3.75)


def test_task_04_b():
    assert(avg_word_length("????twelvedigits") == 12.0)


def test_task_04_c():
    assert(avg_word_length("") == 0.0)


def test_task_04_d():
    assert(avg_word_length("?this?is?a?string") == 3.25)


def test_task_04_e():
    assert(avg_word_length(":s;t,r.i.n.g") == 1.0)


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
