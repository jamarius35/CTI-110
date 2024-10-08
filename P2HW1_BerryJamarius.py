# Jamarius Berry

# 9/25/2024

# P1HW2

# This program calculates and displays travel expenses


print("Travel Budget!\n")


# Get the budget and cost of everything

budget = float(input("Enter your total budget: "))

destination = input("Enter your travel destination: ")

gas_expense = float(input("Enter the amount you will spend on gas: "))

accomodation_expense = float(input("Enter the amount you will spend on accomodations: "))

food_expense = float(input("Enter the amount you will spend on food: "))

print()

print()


# Calculate total expenses

total_expenses = gas_expense + accomodation_expense + food_expense

# Subtract expenses from budget

remaining_budget = budget - total_expenses

print()

print()

print("----------Travel Expenses---------")

print()

print(f"{'Travel Destination':<20}{destination}")

print(f"{'Initial Budget':<20}${budget:,.2f}")

print()

print(f"{'Fuel':<20}${gas_expense:,.2f}")

print(f"{'Accomodation':<20}${accomodation_expense:,.2f}")

print(f"{'Food':<20}${food_expense:,.2f}")

print()

print(f"{'Total Expenses':<20}${total_expenses:,.2f}")

print(f"{'Remaining Budget':<20}${remaining_budget:,.2f}")


