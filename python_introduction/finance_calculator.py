#!/usr/bin/env python3
"""
Finance Calculator
This script calculates monthly savings based on income and expenses,
and projects annual savings with interest
"""

# Prompt user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest (5% annual interest rate)
annual_savings = monthly_savings * 12  # Savings without interest
interest_earned = annual_savings * 0.05  # 5% interest on annual savings
projected_annual_savings = annual_savings + interest_earned

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")