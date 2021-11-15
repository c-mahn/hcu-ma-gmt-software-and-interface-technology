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

# Functions
# -----------------------------------------------------------------------------


def makelist(inputlist):
    if(type(inputlist) != List):
        return(TypeError)
    for i, e in enumerate(inputlist):
        if(type(e) != int && type(e) != float):
            return(TypeError)
        elif(i == 0):
            result = e
        else:
            result += f"; {i}"


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass