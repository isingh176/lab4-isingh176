#!/usr/bin/env python3
# Author ID- isingh176

def is_digits(sobj):
    # Loop through each character in the string object
    for char in sobj:
        if not char.isdigit():  # Check if the character is not a digit
            return False  # Return False if any character is not a digit
    return True  # Return True if all characters are digits

if __name__ == '__main__':
    test_list = ['x3058', '358', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(f"{item} is an integer.")
        else:
            print(f"{item} is not an integer.")
