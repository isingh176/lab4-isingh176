#!/usr/bin/env python3
# Author ID- isingh176

str1 = 'Hello World!!'
str2 = 'Seneca College'
num1 = 1500
num2 = 1.50

def first_five(string):  # Accepts a single string argument
    return string[:5]  # Returns the first five characters

def last_seven(string):   # Accepts a single string argument
    return string[-7:]  # Returns the last seven characters

def middle_number(number):  # Accepts an integer as an argument
    num_str = str(number)  # Convert number to string
    return num_str[1:3]  # Returns the second and third characters

def first_three_last_three(string1, string2):  # Accepts two string arguments
    return string1[:3] + string2[-3:]  # Returns first three from string1 and last three from string2

if __name__ == '__main__':
    print(first_five(str1))  # Output: Hello
    print(first_five(str2))  # Output: Sene
    print(last_seven(str1))  # Output: World!!
    print(last_seven(str2))  # Output: College
    print(middle_number(num1))  # Output: 50
    print(middle_number(num2))  # Output: .5
    print(first_three_last_three(str1, str2))  # Output: Helge
    print(first_three_last_three(str2, str1))  # Output: Sen!!
