#!/usr/bin/env python3
number1 = 10
number2 = 5
def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2
def subtract_numbers(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2
def multiply_numbers(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2
print(f"Addition of {number1} and {number2} is {add_numbers(number1, number2)}")
print(f"Subtraction of {number1} and {number2} is {subtract_numbers(number1, number2)}")
print(f"Multiplication of {number1} and {number2} is {multiply_numbers(number1, number2)}")    