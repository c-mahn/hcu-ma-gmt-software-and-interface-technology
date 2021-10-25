# Mandatory Exercise 02
# #############################################################################

# Task 1
# Write a function that takes a list as an argument and computes and returns
# the sum of all values. If a value inside the list is not an integer or float
# (=can not be summed up), return 0 instead.

# Task 2
# Write a function that takes a list as argument and gives back the list
# entries divided by a comma. However, the last and the second last elements
# should be divided by an "end" and there should not be a comma after the last
# element but a point.
# The expected return value for the list
# l = ["first", "second", "third", "fourth"] would be
# "first, second, third and fourth."".

# Task 3
# Write a function that takes a list consisting of lists as an argument.
# Return the inner list with the highest sum of the values. You don't need to
# consider what happens if there is a string inside the lists.
# Given the list `list1 = [[0,1,2], [5,3,1]]`, the program would return
# `[5, 3, 1]` since the sum out of 5, 3 and 1 is higher than the sum out of
# 0, 1 and 2.

# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

# import math as m

# Functions
# -----------------------------------------------------------------------------

def sum_up(l):
    """
    Task 1
    """
    try:
        result = 0
        for i in l:
            result += i
        return(result)
    except:
        return(0)


def learning_conditionals(l):
    """
    Task 2
    """
    if(len(l) == 0):
        return(0)
    else:
        result = l.pop(0)
        for i, e in enumerate(l):
            if((i+1) < len(l)):
                result = f"{result}, {e}"
            else:
                result = f"{result} and {e}"
        result = f"{result}."
        return(result)


def max_sum(l):
    """
    Task 3
    """
    result = []
    for i, e in enumerate(l[0]):
        number = 0
        for j, e in enumerate(l):
            if(l[j][i] > number):
                number = l[j][i]
        result.append(number)
    return(result)


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # Unit-Testing

    # Task 1
    print("[Task 1]")
    print(sum_up([1,2,3,4,5]) == 15)
    print(sum_up(["a"]) == 0)

    # Task 2
    print("[Task 2]")
    print(learning_conditionals(["first", "second", "third", "fourth", "fifth"]) == "first, second, third, fourth and fifth.")
    print(learning_conditionals(['50', '29', '58', '8', '53', '69', '6', '27', '69', '76', '68', '58', '86', '76', '13', '63', '53', '16', '14', '90']) == "50, 29, 58, 8, 53, 69, 6, 27, 69, 76, 68, 58, 86, 76, 13, 63, 53, 16, 14 and 90.")
    print(learning_conditionals(["one"]) == "one.")
    print(learning_conditionals([]) == 0)

    # Task 3
    print("[Task 3]")
    print(max_sum([[1,2,3], [2,2,3], [4,5,243]]) == [4, 5, 243])