# Mandatory exercise 3
# #############################################################################

# We will do something of actual use this time: you are supposed 
# to write a function that generates a password and the according tests!
# However, there are rules to the password generator because we have
# two types of passwords we can generate: strong ones and weak ones

# The strong passwords should have a length of 8 – 12 characters
# They have to contain at least one symbol: !"#$%&'()*+,-./:;<=>?
# @[\]^_`{|}~
# They have to contain at least one character:
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# They have to contain at least one digit:
# 0123456789

# The strong passwords are not allowed to have duplicate elements
# (upper/lowercase does not matter):
# aX57A21#!    not allowed
# ax57b21#!    allowed

# The weak passwords should have a length of 6 – 8 characters
# They are not allowed to contain symbols!
# They have to contain at least one character:
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# They have to contain at least one digit:
# 0123456789

# The weak passwords are not allowed to have duplicate elements as well:
# a12A21gG     not allowed
# ag5721w      allowed

# Author:
# Christopher Mahn

# #############################################################################

# Import of Libraries
# -----------------------------------------------------------------------------

# import math as m
import string as st
import random as r

# Functions
# -----------------------------------------------------------------------------


def pwgen(password_type=None):
    """
    This function generates a strong or weak password.

    Args:
        password_type ([string]): [either "strong" or "weak"]
    """
    
    # Setting for Password-Generation
    if(password_type == "strong"):
        valid_password_type = True
        pw_length_min = 8
        pw_length_max = 12
        contain_lowercase_letters = True
        contain_uppercase_letters = True
        contain_numbers = True
        contain_symbols = True
    elif(password_type == "weak"):
        valid_password_type = True
        pw_length_min = 6
        pw_length_max = 8
        contain_lowercase_letters = True
        contain_uppercase_letters = True
        contain_numbers = True
        contain_symbols = False
    else:
        valid_password_type = False
        
    # Generate Password with Setting
    if(valid_password_type):
        
        # Adding character-selection
        pw_chars = ""
        if(contain_lowercase_letters or contain_uppercase_letters):
            pw_chars += st.ascii_lowercase
        if(contain_numbers):
            pw_chars += st.digits
        if(contain_symbols):
            pw_chars += st.punctuation

        # make randomised password with lowercase letters
        valid_password = False
        while(valid_password == False):
            pw_length = r.randint(pw_length_min, pw_length_max)
            pw_chars = list(pw_chars)
            r.shuffle(pw_chars)
            password = ""
            for i in range(pw_length):
                password += pw_chars[i]

            # Uppercase and lowercase randomisation if needed
            if(contain_uppercase_letters == True and contain_lowercase_letters == True):
                password = list(password)
                for i, e in enumerate(password):
                    if(e in st.ascii_lowercase):
                        if(r.getrandbits(1) == 1):
                            password[i] = e.upper()
                password = "".join(password)
            elif(contain_uppercase_letters == True and contain_lowercase_letters == False):
                password = password.upper()

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # Check if password has all character-selections contained
            valid_password = True

            # Check for lowercase letters
            if(contain_lowercase_letters):
                check_pass = False
                for i in password:
                    if(i in st.ascii_lowercase):
                        check_pass = True
            if(check_pass is not True):
                valid_password = False

            # Check for uppercase letters
            if(contain_uppercase_letters):
                check_pass = False
                for i in password:
                    if(i in st.ascii_uppercase):
                        check_pass = True
            if(check_pass is not True):
                valid_password = False

            # Check for numbers
            if(contain_numbers):
                check_pass = False
                for i in password:
                    if(i in st.digits):
                        check_pass = True
            if(check_pass is not True):
                valid_password = False

            # Check for symbols
            if(contain_symbols):
                check_pass = False
                for i in password:
                    if(i in st.punctuation):
                        check_pass = True
            if(check_pass is not True):
                valid_password = False
        return(password)
    else:
        return(ValueError)


# Classes
# -----------------------------------------------------------------------------

# Beginning of the Programm
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    pass