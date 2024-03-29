# 5.75 Task & Break
# #############################################################################

# Think of test cases. What positive, negative and edge cases can you think of?
# Implement the test cases. After implementing the test cases, implement the
# function that fulfills your test cases.


# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

# import math as m
from lecture3 import makelist

# Functions
# -----------------------------------------------------------------------------


def test_makelist_01():
    assert(makelist([5.0, 7, 13, 9.45, 3.14, 7.77]) == "5.0; 7; 13; 9.45; 3.14; 7.77")
    
    
def test_makelist_02():
    assert(makelist([]) == "")
    
    
def test_makelist_03():
    assert(makelist(["one"]) == TypeError)
    
    
def test_makelist_04():
    assert(makelist(1) == TypeError)
    
    
def test_makelist_05():
    assert(makelist([1]) == "1")
    
    
def test_makelist_06():
    assert(makelist([1, 2, 3, 4, 5, 6, 0]) == "1; 2; 3; 4; 5; 6; 0")
    
    
def test_makelist_07():
    assert(makelist([-1]) == "-1")
    
    
def test_makelist_08():
    assert(makelist([1, 0, -1]) == "1; 0; -1")
    
    
def test_makelist_09():
    assert(makelist([1.1, 0, -1.1]) == "1.1; 0; -1.1")


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass