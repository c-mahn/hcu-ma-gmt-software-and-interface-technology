# 5.75 Task & Break
# #############################################################################

# Write a function that returns the sum of the multiples of 3 and 5


# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

import math as m

# Functions
# -----------------------------------------------------------------------------

def multiples_3_5(x):
    """
    Funktion for returning the multiples of 3 and 5 in a specific threshold.

    Args:
        x: The threshold, where to stop
    Returns: Result of the calculation
    """
    numbers = []
    number = 3
    while(number < x):
        numbers.append(number)
        number += 3
    number = 5
    while(number < x):
        numbers.append(number)
        number += 5
    result = 0
    for i in numbers:
        result += i
    return(result)


def lambda_function(a, b, c):
    return((m.sqrt(a**2+b**2)+c)/2)


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    for i in range(15):
        print(f"{i:02d}: {multiples_3_5(i)}")
    print(lambda_function(5, 10, 15))
