"""
module_to_test.py

This is the module we will test during the lesson.
It contains simple functions that are easy for beginners to understand.
Students can change the code and immediately rerun the tests to see what happens.
"""


def add(a, b):
    """
    Return the sum of two numbers.
    in: two numbers
    out: their sum
    """
    return a + b


def subtract(a, b):
    """
    Return the result of a minus b.
    in: two numbers
    out: their subtraction result
    """
    return a - b


def is_even(number):
    """
    Check whether a number is even.
    in: one integer
    out: True if the number is even, otherwise False
    """
    return number % 2 == 0


def capitalize_text(text):
    """
    Return the text with the first letter capitalized.
    in: a string
    out: a capitalized string
    """
    return text.capitalize()


def divide(a, b):
    """
    Divide a by b.
    in: two numbers
    out: division result
    note: this function may raise ZeroDivisionError if b is 0
    """
    return a / b


def find_max(a, b):
    """
    Return the bigger value between two numbers.
    in: two numbers
    out: the larger number
    """
    if a >= b:
        return a
    return b


def find_min(a, b):
    """
    Return the smaller value between two numbers.
    in: two numbers
    out: the smaller number
    """
    if a <= b:
        return a
    return b


def reverse_string(text):
    """
    Return the reversed version of the given text.
    in: a string
    out: reversed string
    """
    return text[::-1]
