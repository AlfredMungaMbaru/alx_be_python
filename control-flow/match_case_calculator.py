#!/usr/bin/env python3
"""
Match Case Calculator

This script implements a simple calculator that asks users for two numbers
and an operation, then performs the calculation using a match case statement.
"""

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get operation choice from user
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation selected. Please use +, -, *, or /.")