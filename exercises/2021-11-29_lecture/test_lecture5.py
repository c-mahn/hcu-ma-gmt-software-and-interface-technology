# Lecture 5
# #############################################################################


# # Task 01: Given a list of words, return(!) another list
# # of words adding "un" at the beginning of each word.

# list_of_words = ["happy", "willing", "fold"]

# def adding_prefix(wordlist):
#     pass

# # Task 02: Given a list of words, return(!) another list of
# # words removing the "ness" at the end of them. If a word would
# # end on "i" like in "happiness", replace the "i" by "y".

# list_of_words = ["happiness", "sadness", "greatness", "loneliness"]

# def removing_ness(wordlist):
#     pass

# # Task 03: Write a function that returns "valid" if the coordinates that
# # are being passed are in the box with the vertices (53.5813, 10.0016)
# # and (53.5299, 10.0648). Return "invalid" otherwise.

# def valid_coordinates(coordinatetuple):
#     pass

# # Task 04: Write a function that takes a string as an argument (don't allow 
# # anything outside of strings!). By iterating over the string with a for loop,
# # count the number of iterations (for "abc" the for loop would iterate three times)
# # and return the total amount of iterations.

# def iterator(some_word):
#     pass

# # Task 05: Write a function that creates an identical list from the list that
# # is being passed to the function using list comprehension.

# list1 = [234,6,54,65,768,4132,46530,6543,445,71]

# def copying_lists(somelist):
#     pass

# # Task 06: Create a list from the elements of a range between
# # 1000 and 5000 with steps of 500 and return it.

# def list_elements():
#     pass

# # Task 07: You are given two lists of equal length. Return a list with tuples
# # that contain the corresponding list elements of each list. If the lengths of
# # the lists don't match, return "False".
# # Example:
# # l1 = [1, 2, 3]
# # l2 = ["a", "b", "c"]
# # expected return: [(1,"a"), (2,"b"), (3,"c")]

# def creating_tuples(first_list, second_list):
#     pass

# # Task 08: Write a function that, if given a dictionary, return the keys as a list.

# def dictkeys(some_dictionary):
#     pass

# # Task 09: Write a guessing game (not necessarily as a function) that asks the user
# # to input a number between 0 and 10. Let the user guess. If the users number is
# # wrong, ask him again until he guesses right. You can decide if you want to give 
# # tips for wrong guesses. Count the guesses and return the number of guesses at the end.

# # Task 10: Utilizing object oriented programming, write a class for a cars/books/
# # memberships and add meaningful attributes and methods for it.

# # Task 11: Write a function that, if given 3 int values, returns their sum.
# # However, if one of the values is 13 then it does not count towards the sum
# # and values to its right do not count. So for example, if b is 13, then 
# # both b and c do not count. (task from codingbat p107863)

# def lucky_sum(a,b,c):
#     pass


# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

# import math as m
from lecture5 import *
import re
import string as st


# Functions
# -----------------------------------------------------------------------------


def test_task_01():
    list_of_words = ["happy", "willing", "fold"]
    assert(adding_prefix(list_of_words) == ["unhappy", "unwilling", "unfold"])


def test_task_02():
    list_of_words = ["happiness", "sadness", "greatness", "loneliness"]
    print(removing_ness(list_of_words))
    
def test_task_03():
    assert(valid_coordinates((53.5555, 10.0333)) == "valid")
    assert(valid_coordinates((53.4444, 10.0333)) == "invalid")
    assert(valid_coordinates((53.6666, 10.0333)) == "invalid")
    assert(valid_coordinates((53.5555, 10.1000)) == "invalid")
    assert(valid_coordinates((53.5555, 10.0000)) == "invalid")


def test_task_04():
    assert(iterator("djeidirh") == 8)
    assert(iterator("dk h fuis") == 9)
    assert(iterator(4) == TypeError)


def test_task_05():
    list1 = [234,6,54,65,768,4132,46530,6543,445,71]
    list2 = copying_lists(list1)
    assert(list1 == list2)


def test_task_06():
    assert(list_elements() == [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000])


def test_task_07():
    l1 = [1, 2, 3]
    l2 = ["a", "b", "c"]
    assert(creating_tuples(l1, l2) == [(1,"a"), (2,"b"), (3,"c")])
    l1.pop()
    assert(creating_tuples(l1, l2) == False)


def test_task_08():
    dict1 = {"x": 12.7, "y": 13.9, "z": 9.4}
    assert(dictkeys(dict1) == ["x", "y", "z"])


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
