#!/usr/bin/env python3
"""
Pattern Drawing Script

This script prompts the user to enter a positive integer and then draws
a square pattern of that size using asterisks (*).
"""

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after completing a row
    print()
    
    # Increment the row counter
    row += 1