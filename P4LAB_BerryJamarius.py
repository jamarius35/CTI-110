# Jamarius Berry
# 11/12/2024
# P4LAB
# Use loops and fucntions to calculate coin combinations for given value


import random

def disperse_change(change):
    """
    Calculate the number of dollars and coins needed for the given change amount.
    
    Args:
        change (float): Amount of change to disperse
    """
    # Convert change to cents to avoid floating point precision issues
    cents = round(change * 100)
    
    # Calculate dollars and remaining cents
    dollars = cents // 100
    cents = cents % 100
    
    # Calculate coins
    quarters = cents // 25
    cents = cents % 25
    
    dimes = cents // 10
    cents = cents % 10
    
    nickels = cents // 5
    pennies = cents % 5
    
    # Print results
    print("\nChange breakdown:")
    if dollars > 0:
        print(f"Dollars: {dollars}")
    if quarters > 0:
        print(f"Quarters: {quarters}")
    if dimes > 0:
        print(f"Dimes: {dimes}")
    if nickels > 0:
        print(f"Nickels: {nickels}")
    if pennies > 0:
        print(f"Pennies: {pennies}")

def main():
    # Generate random purchase amount
    amount_due = round(random.uniform(0.01, 100.00), 2)
    print(f"Amount due: ${amount_due:.2f}")
    
    # Get payment from user
    while True:
        try:
            payment = float(input("How much cash will you put in the self-checkout? $"))
            if payment < amount_due:
                print("Insufficient payment. Please enter an amount equal to or greater than the amount due.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Calculate change
    change = round(payment - amount_due, 2)
    print(f"\nChange due: ${change:.2f}")
    
    # Disperse change if needed
    if change > 0:
        disperse_change(change)
    else:
        print("No change due.")

if __name__ == "__main__":
    main()
