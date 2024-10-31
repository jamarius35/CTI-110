# Jamarius Berry

# 10/31/2024

# P4LAB2

# Program asks user for integer and displays multiplication table for number


# While loop to control program running continuously
run_again = "yes"

while run_again == "yes" or run_again == "y":
    user_int = int(input("Enter an integer: "))
    print()
    if user_int >= 0:
        # Print multiplication table
        for num in range(1, 13):
            print(f"{user_int} * {num} = {user_int * num}")
        
    else:
        print("Cannot accept negative values!!")
        
    print()
    run_again = input("Would you like to run program again?").lower()
    valid_inputs = ["yes", "y", "no", "n"]
    # validate the user input
    while run_again not in valid_inputs:
        print("INVALID REPSONSE ENTERED!")
        run_again = input("Would you like to run the program again?")

# Loop breaks
print("Exiting program...")

            
