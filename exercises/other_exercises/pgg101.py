# PGG1011: Final Python exercise
# #############################################################################

# In this task, you will draw on various concepts you have already learned.

# (a) Loop over all numbers from 0 to 1000 and print the sum of all the even
# numbers.

# (b) Write a small "game" in which you determine a number between 1 and 10.
# Let the user guess the number until he finds your number.

# (c) Write a function that prints all numbers up to the one passed to it as an
# argument (including the number that's being passed). Print the numbers in
# correct order as well as reverse order (find out how to print them in reverse
# order).


# Autoren:
# Christopher Mahn

# #############################################################################

# Import von Bibliotheken
# -----------------------------------------------------------------------------

import random as r

# Funktionen
# -----------------------------------------------------------------------------

# Klassen
# -----------------------------------------------------------------------------

# Beginn des Programms
# -----------------------------------------------------------------------------

if __name__ == '__main__':

    # Task a)
    solution_a = 0
    for i in range(1001):
        if(i%2 == 0):  # Check if even
            solution_a += i
    print(f'The solution for task a) is:\n{solution_a}')

    # Task b)
    random_number = r.randint(1, 10)
    guessed_number = 0
    print("I think of a number between 1 and 10. You have to guess it.")
    while(random_number != guessed_number):  # Break if numbers match
        guessed_number = int(input("My guess is "))  # Guess number
        if(guessed_number > random_number):  # Guessed to high
            print("That is not the number I'm thinking of. Please try again. (Hint: The number is smaller.)")
        elif(guessed_number < random_number):  # Guessed to low
            print("That is not the number I'm thinking of. Please try again. (Hint: The number is larger.)")
    print(f'That guess is correct. My number is {random_number}.')

    # Task c)
    picked_number = int(input("Pick a number: "))
    number_list = []
    for i in range(picked_number+1):  # Generate ascending list
        number_list.append(i)
    for i in range(picked_number+1):  # Generate descending list
        number_list.append(picked_number-i)
    for i in number_list:  # Print entire list
        print(i)
