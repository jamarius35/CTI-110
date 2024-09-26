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

print(f"Travel Destination: {destination}")

print(f"Initial Budget: {budget}")

print()

print(f"Fuel: {gas_expense}")

print(f"Accomodation: {accomodation_expense}")

print(f"Food: {food_expense}")

print()

print(f"Total Expenses: ${total_expenses:.2f}")

print(f"Remaining Budget: ${remaining_budget:.2f}")


