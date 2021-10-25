# Mandatory Exercise 01
# #############################################################################

# Task 1
# Write a function that returns the first value (base) to the power of the
# second value (exponent).

# Task 2
# Calculate the area of a circle. Pass the radius as argument to the function.

# Task 3
# Calculate the length of the hypothenuse c for the catheti a and b.


# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

# import math as m

# Functions
# -----------------------------------------------------------------------------

def simplefunction(a,b):
    """
    Task 1
    """
    return(a**b)


from math import pi
def circle(r):
    """
    Task 2
    """
    return(pi*(r**2))


from math import sqrt
def hyp(a,b):
    """
    Task 3
    """
    return(sqrt((a**2)+(b**2)))


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # Unit-Testing

    # Task 1
    print("[Task 1]")
    print(simplefunction(1,1) == 1)
    print(simplefunction(20,2) == 400)
    print(simplefunction(-15,5) == -759375)

    # Task 2
    print("[Task 2]")
    print(circle(7) == 153.93804002589985)
    print(circle(0) == 0.0)
    print(circle(-5) == 78.53981633974483)

    # Task 3
    print("[Task 3]")
    print(hyp(5.12, 3.14) == 6.006163500938015)
    print(hyp(5, 0) == 5.0)
    print(hyp(-6,17) == 18.027756377319946)
