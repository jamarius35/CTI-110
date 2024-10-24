# Jamarius Berry

# 10/22/2024

# P3LAB

# Calculate coin combinations for given value


# Regular Division
#print(100/3)

# Floor Division - return the whole number
#print(100//3)

# Modulus Division - return the remainder only as a integer
#print(100&3)
#print(7%4)

# Get the money from user as a float
money = float(input("Enter the amount of money as a float: $"))


# Considering if the user put in 0.00
if money == 0:
    print("No change")

if money < 0:
    print("BAD")

    # Convert money to a whole number
    money = round(money * 100)

    #print(money)

    # Calculate the amount of dollars in the money variable
    num_dollars = money // 100
    #print(f"Dollars: {num_dollars}")

    # Remove the dollars from money variable
    money = money - (num_dollars * 100)

    # Calculate the amount of quarters in the money variable
    num_quarters = money // 25
    #print(f"Quarters: {num_quarters}")

    # Remove the quarters from money variable
    money = money - (num_quarters * 25)

    # Calculate the amount of dimes in the money variable
    num_dimes = money // 10
    #print(f"Dimes: {num_dimes}")

    # Remove the dimes from money variable
    money = money - (num_dimes * 10)

    # Calculate the amount of nickels in the money variable
    num_nickels = money // 5
    #print(f"Nickels: {num_nickels}")

    # Remove the nickels from money variable
    money = money - (num_nickels * 5)

    # Calculate the amount of pennies in the money variable
    num_pennies = money
    #print(f"Pennies: {num_pennies}")


else:
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    


# Convert money to a whole number
money = round(money * 100)

#print(money)

# Calculate the amount of dollars in the money variable
num_dollars = money // 100
#print(f"Dollars: {num_dollars}")

# Remove the dollars from money variable
money = money - (num_dollars * 100)

# Calculate the amount of quarters in the money variable
num_quarters = money // 25
#print(f"Quarters: {num_quarters}")

# Remove the quarters from money variable
money = money - (num_quarters * 25)

# Calculate the amount of dimes in the money variable
num_dimes = money // 10
#print(f"Dimes: {num_dimes}")

# Remove the dimes from money variable
money = money - (num_dimes * 10)

# Calculate the amount of nickels in the money variable
num_nickels = money // 5
#print(f"Nickels: {num_nickels}")

# Remove the nickels from money variable
money = money - (num_nickels * 5)

# Calculate the amount of pennies in the money variable
num_pennies = money
#print(f"Pennies: {num_pennies}")

# Print dollar amount gramatically correct
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    else: # variable is greater than one
        print(f"{num_dollars} dollars")


# Print quarter amount gramatically correct
if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    else: # variable is greater than one
        print(f"{num_quarters} quarters")


# Print dime amount gramatically correct
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    else: # variable is greater than one
        print(f"{num_dimes} dimes")


# Print nickel amount gramatically correct
if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} nickel")
    else: # variable is greater than one
        print(f"{num_nickels} nickels")


# Print pennies amount gramatically correct
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} penny")
    else: # variable is greater than one
        print(f"{num_pennies} pennies")        
