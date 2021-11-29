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
# import string as st
import random as r
import os

# Functions
# -----------------------------------------------------------------------------


# Task 01
def adding_prefix(wordlist):
    """
    Given a list of words, return(!) another list of words adding "un" at the
    beginning of each word.

    Args:
        wordlist ([list]): [a list of words as strings]
    """
    for i, e in enumerate(wordlist):
        wordlist[i] = f"un{e}"
    return(wordlist)


# Task 02
def removing_ness(wordlist):
    """
    Given a list of words, return(!) another list of words removing the "ness"
    at the end of them. If a word would end on "i" like in "happiness", replace
    the "i" by "y".

    Args:
        wordlist ([list]): [a list of words as strings]
    """
    for i, e in enumerate(wordlist):
        e = e[:len(e)-4]
        if(e[len(e)-1:len(e)] == "i"):
            e = f"{e[:len(e)-1]}y"
        wordlist[i] = e
    return(wordlist)


# Task 03
def valid_coordinates(coordinatetuple):
    """
    Task 03: Write a function that returns "valid" if the coordinates that are
    being passed are in the box with the vertices (53.5813, 10.0016) and
    (53.5299, 10.0648). Return "invalid" otherwise.

    Args:
        coordinatetuple ([tuple]): [a coordinate as tuple]
    """
    if(53.5299 < coordinatetuple[0] < 53.5813 and 10.0016 < coordinatetuple[1] < 10.0648):
        return("valid")
    else:
        return("invalid")


# Task 04
def iterator(some_word):
    """
    Write a function that takes a string as an argument (don't allow anything
    outside of strings!). By iterating over the string with a for loop, count
    the number of iterations (for "abc" the for loop would iterate three times)
    and return the total amount of iterations.

    Args:
        some_word ([string]): [a string to check the length of]
    """
    if(type(some_word) == str):
        length = 0
        for i in some_word:
            length += 1
        return(length)
    else:
        return(TypeError)


# Task 05
def copying_lists(somelist):
    """
    Task 05: Write a function that creates an identical list from the list that
    is being passed to the function using list comprehension.

    Args:
        somelist ([list]): [a list with elements]
    """
    result = [i for i in somelist]
    return(result)


# Task 06
def list_elements():
    """
    Task 06: Create a list from the elements of a range between 1000 and 5000
    with steps of 500 and return it.
    """
    result = []
    for i in range(1000, 5001, 500):
        result.append(i)
    return(result)


# Task 07
def creating_tuples(first_list, second_list):
    """
    You are given two lists of equal length. Return a list with tuples that
    contain the corresponding list elements of each list. If the lengths of the
    lists don't match, return "False".
    Example:
    l1 = [1, 2, 3]
    l2 = ["a", "b", "c"]
    expected return: [(1,"a"), (2,"b"), (3,"c")]

    Args:
        first_list ([list]): [a list with elements]
        second_list ([list]): [a list with elements]
    """
    if(len(first_list) == len(second_list)):
        result = []
        for i,e in enumerate(first_list):
            result.append((e, second_list[i]))
        return(result)
    else:
        return(False)


# Task 08
def dictkeys(some_dictionary):
    """
    Write a function that, if given a dictionary, return the keys as a list.

    Args:
        some_dictionary ([dictionary]): [a dictionary with elements]
    """
    result = []
    for i in some_dictionary:
        result.append(i)
    return(result)


# Classes
# -----------------------------------------------------------------------------

# # Task 10: Utilizing object oriented programming, write a class for a cars/books/
# # memberships and add meaningful attributes and methods for it.
# Task 10
class Car():
    pass


# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # Task 09

    # Write a guessing game (not necessarily as a function) that asks the user
    # to input a number between 0 and 10. Let the user guess. If the users
    # number is wrong, ask him again until he guesses right. You can decide if
    # you want to give tips for wrong guesses. Count the guesses and return the
    # number of guesses at the end.
    number_to_guess = r.randint(0,10)
    guess = -1
    guesses = 0
    print("Computer: I'm thinking of a number between 0 and 10. What do you think it is?")
    while(number_to_guess != guess):
        guess = int(input(f"{os.getlogin()}: My guess is "))
        guesses += 1
        if(number_to_guess < guess):
            print(f'Computer: You guessed "{guess}", but my number is smaller.')
        elif(number_to_guess > guess):
            print(f'Computer: You guessed "{guess}", but my number is larger.')
        elif(number_to_guess == guess):
            print(f'Computer: That is correct. The number I was thinking of was "{number_to_guess}".')
        else:
            print(f'Computer: I have no clue, what you mean by "{guess}".')
    print(f'Computer: You needed {guesses} attempts, to guess my number.')
