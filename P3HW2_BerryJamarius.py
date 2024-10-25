# Jamarius Berry

# 10/24/2024

# P3HW2

# Calculate regular and overtime pay given an employees hours worked

'''
Input: Get the name as a string
Input: Get the hours worked as an integer
Input: Get the pay rate as a float

Output: Print employee name

If hours worked is greater than 40
    Calculate any OT hours worked by subtracting 40 from hours worked
    Calculate OT pay (OT hours * (pay rate * 1.5))
    Calculate regular pay (40 * reg pay rate)
    Calculate gross by adding OT pay and reg pay

else (employee worked 40 or less hours):
    overtime hours = 0
    overtime pay = 0
    calculate reg pay by multiplying original hours worked by reg pay rate
    calculate gross pay is equal to regualar pay




Output:
Display total hours worked
Display regular pay rate
Display overtime hours worked
Dispaly OT pay (OT hours x OT pay rate)
Display pay for regular hours worked at reg pay rate
Display gross pay - both reg pay and OT pay
'''

def calculate_pay():
    # Get employee information
    employee_name = input("Enter employee name: ")
    hours_worked = float(input("Enter number of hours worked this week: "))
    pay_rate = float(input("Enter hourly pay rate: $"))
    
    # Highlight variables
    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked
    
    # Calculate overtime hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    
    # Calculate regular pay
    regular_pay = regular_hours * pay_rate
    
    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay
    
    # Display results
    print("\nPayroll Summary")
    print("-" * 130)  
    

    print(f"{'Name':<15} {'Pay Rate':>10} {'Hours':>15} {'Regular Hrs':>15} {'OT Hours':>15} {'Regular Pay':>15} {'OT Pay':>15} {'Gross Pay':>15}")
    print("-" * 130)  
    
    
    print(f"{employee_name:<15} {pay_rate:>10.2f} {hours_worked:>15.2f} {regular_hours:>15.2f} {overtime_hours:>15.2f} {regular_pay:>15.2f} {overtime_pay:>15.2f} {gross_pay:>15.2f}")
    print("-" * 130)  

# Calculate hrs and OT hrs worked
if __name__ == "__main__":
    calculate_pay()
