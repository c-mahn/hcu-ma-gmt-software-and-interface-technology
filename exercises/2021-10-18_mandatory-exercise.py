# Mandatory Exercise 01
# #############################################################################

# Task 1
# Write a function that returns the first value (base) to the power of the
# second value (exponent).

# Task 2
# Calculate the area of a circle. Pass the radius as argument to the function.

# Task 3
# Calculate the length of the hypothenuse c for the catheti a and b.

# Task 5
# 42154 seconds after midnight is what time of day (in hours, minutes and
# seconds (HH:MM:SS))? Write down the Python expressions but think it through
# first. Think of the floor division // and modulo % operators. To pass you
# have to format your string to print out HH:MM:SS!

# Task 6
# Point p1 is given with the coordinates x1, y1. Point p2 has been measured to
# be d [meters] away in the direction t [degrees]. Think about radians and
# degrees in programming and calculate the coordinates x2 and y2 of point p2.
# The forumlas to do so are:
# x2 = x1 + distance*cos(angle)
# and
# y2 = y1 + distance*sin(angle)


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


def hours(s):
    """
    Task 5
    """
    second = s%60
    s = s//60
    minute = s%60
    hour = s//60
    return(f"{hour:2d}:{minute:2d}:{second:2d}")


from math import pi, sin, cos
def coordinates(x1, y1, d, t):
    """
    Task 6
    """
    x2 = x1 + d*cos(t/180*pi)
    y2 = y1 + d*sin(t/180*pi)
    return(f"{x2}, {y2}")


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

    # Task 5
    print("[Task 5]")
    print(hours(42154) == "11:42:34")

    # Task 6
    print("[Task 6]")
    print(coordinates(105.7,294.3,24.1,97.3) == "102.63774293270745, 318.2046560664197")
    print(coordinates(1,1,50,90) == "1.000000000000003, 51.0")
    print(coordinates(55,-19,33,112) == "42.6379824172749, 11.597067200703986")
