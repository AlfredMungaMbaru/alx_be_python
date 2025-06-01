#!/usr/bin/env python3
"""
Weather Advice Script

This script prompts the user to input the current weather condition
and provides appropriate clothing recommendations based on the input.
"""

# Get weather input from the user
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendations based on weather input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")