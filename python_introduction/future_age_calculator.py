#!/usr/bin/env python3
"""
Future Age Calculator
This script calculates how old a person will be in the year 2050
"""

# Prompt user for their current age
current_age = input("How old are you? ")

# Convert the input string to an integer
current_age = int(current_age)

# Calculate age in 2050 (assuming current year is 2023)
future_age = current_age + 27  # 2050 - 2023 = 27 years

# Print the result
print(f"In 2050, you will be {future_age} years old.")