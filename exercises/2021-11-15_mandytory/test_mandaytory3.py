# Mandatory exercise 3
# #############################################################################

# Description of the task


# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

# import math as m
from mandaytory3 import pwgen
import re
import string as st


# Functions
# -----------------------------------------------------------------------------


def test_pwgen_type_1():
    """
    Test for invalid password types.
    """
    assert(pwgen("") == ValueError)


def test_pwgen_type_2():
    """
    Test for invalid password types.
    """
    assert(pwgen() == ValueError)


def test_pwgen_type_3():
    """
    Test for invalid password types.
    """
    assert(pwgen(0) == ValueError)


def test_pwgen_type_4():
    """
    Test for invalid password types.
    """
    assert(pwgen(True) == ValueError)


def test_pwgen_type_5():
    """
    Test for invalid password types.
    """
    assert(pwgen(None) == ValueError)


def test_pwgen_type_6():
    """
    Test for invalid password types.
    """
    assert(pwgen("mediocre") == ValueError)


def test_pwgen_strong_str():
    """
    Test, if the generated strong password is a string.
    """
    assert(type(pwgen("strong")) == str)


def test_pwgen_strong_length():
    """
    Test, if the generated strong password is between 8 and 12 characters long.
    """
    for i in range(10000):
        assert(8 <= len(pwgen("strong")) <= 12)


def test_pwgen_strong_length_variable():
    """
    Test, if the generated strong password has all random different lengths.
    """
    lengths = []
    for i in range(10000):
        lengths.append(len(pwgen("strong")))
    assert(len(set(lengths)) == 5)
    

def test_pwgen_strong_valid_chars():
    """
    Check if only allowed characters are present.
    """
    for i in range(10000):
        password = pwgen("strong")
        chars = st.ascii_lowercase
        chars += st.ascii_uppercase
        chars += st.digits
        chars += st.punctuation
        for i in password:
            if(any((i not in chars) for j in chars)):
                assert(False)


def test_pwgen_strong_letters_present():
    """
    Check if letters are present.
    """
    for i in range(10000):
        password = pwgen("strong")
        chars = st.ascii_lowercase
        chars += st.ascii_uppercase
        test_result = False
        for i in password:
            if(any((i in chars) for j in chars)):
                test_result = True
        assert(test_result)


def test_pwgen_strong_digits_present():
    """
    Check if digits are present.
    """
    for i in range(10000):
        password = pwgen("strong")
        chars = st.digits
        test_result = False
        for i in password:
            if(any((i in chars) for j in chars)):
                test_result = True
        assert(test_result)


def test_pwgen_strong_symbols_present():
    """
    Check if symbols are present.
    """
    for i in range(10000):
        password = pwgen("strong")
        chars = st.punctuation
        test_result = False
        for i in password:
            if(any((i in chars) for j in chars)):
                test_result = True
        assert(test_result)


def test_pwgen_strong_duplicates():
    """
    Check if there are duplicates. (Not case sensitive)
    """
    for i in range(10000):
        password = pwgen("strong").lower()
        assert(len(password) == len(set(password)))


def test_pwgen_strong_different():
    """
    Check if passwords are different.
    """
    for i in range(10000):
        assert(pwgen("strong") != pwgen("strong"))


def test_pwgen_weak_str():
    """
    Test, if the generated strong password is a string.
    """
    assert(type(pwgen("weak")) == str)


def test_pwgen_weak_length():
    """
    Test, if the generated weak password is between 6 and 8 characters long.
    """
    for i in range(10000):
        assert(6 <= len(pwgen("weak")) <= 8)


def test_pwgen_weak_length_variable():
    """
    Test, if the generated weak password has all random different lengths.
    """
    lengths = []
    for i in range(10000):
        lengths.append(len(pwgen("weak")))
    assert(len(set(lengths)) == 3)
    

def test_pwgen_weak_valid_chars():
    """
    Check if only allowed characters are present.
    """
    for i in range(10000):
        password = pwgen("weak")
        chars = st.ascii_lowercase
        chars += st.ascii_uppercase
        chars += st.digits
        for i in password:
            if(any((i not in chars) for j in chars)):
                assert(False)


def test_pwgen_weak_letters_present():
    """
    Check if letters are present.
    """
    for i in range(10000):
        password = pwgen("weak")
        chars = st.ascii_lowercase
        chars += st.ascii_uppercase
        test_result = False
        for i in password:
            if(any((i in chars) for j in chars)):
                test_result = True
        assert(test_result)


def test_pwgen_weak_digits_present():
    """
    Check if digits are present.
    """
    for i in range(10000):
        password = pwgen("weak")
        chars = st.digits
        test_result = False
        for i in password:
            if(any((i in chars) for j in chars)):
                test_result = True
        assert(test_result)


def test_pwgen_weak_duplicates():
    """
    Check if there are duplicates. (Not case sensitive)
    """
    for i in range(10000):
        password = pwgen("weak").lower()
        assert(len(password) == len(set(password)))


def test_pwgen_weak_different():
    """
    Check if passwords are different.
    """
    for i in range(10000):
        assert(pwgen("weak") != pwgen("weak"))


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
