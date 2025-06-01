#!/usr/bin/env python3
"""
Multiplication Table Generator

This script prompts the user to enter a number and then displays
its multiplication table from 1 to 10.
"""

# Ask the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")