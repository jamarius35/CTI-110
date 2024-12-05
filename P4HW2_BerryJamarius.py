# Jamarius Berry
# 11/7/2024
# P4HW2
# Calculate regular and overtime pay given for multiple employees




def calculate_payroll():
    # Initialize totals for all employees
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    employee_count = 0
    
    # Print Header
    print("\nPayroll Summary")
    print("-" * 150)
    print(f"{'Name':<15} {'Pay Rate':>15} {'Hours':>15} {'Regular Hrs':>15} {'OT Hours':>15} {'Regular Pay':>15} {'OT Pay':>15} {'Gross Pay':>15}")
    print("-" * 150)
    
    while True:
        # Get employee name or exit
        employee_name = input("\nEnter employee name (or 'Done' to finish): ")
        if employee_name.lower() == 'done':
            break
            
        # Get employee information
        try:
            hours_worked = float(input("Enter number of hours worked this week: "))
            pay_rate = float(input("Enter hourly pay rate: $"))
        except ValueError:
            print("Please enter valid numbers. Try again.")
            continue
            
        # Initialize variables for this employee
        overtime_hours = 0
        overtime_pay = 0
        regular_hours = hours_worked
        
        # Calculate overtime pay
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            regular_hours = 40
            overtime_pay = overtime_hours * (pay_rate * 1.5)
        
        # Calculate regular pay
        regular_pay = regular_hours * pay_rate
        
        # Calculate gross pay
        gross_pay = regular_pay + overtime_pay
        
        # Update total number for all employees
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count += 1
        
        # Print employee information
        print(f"{employee_name:<15} {pay_rate:>15.2f} {hours_worked:>15.2f} {regular_hours:>15.2f} {overtime_hours:>15.2f} {regular_pay:>15.2f} {overtime_pay:>15.2f} {gross_pay:>15.2f}")
    
    # After all employees are entered, print summary for all employees processed
    if employee_count > 0:
        print("-" * 95)
        print("\nPayroll Totals:")
        print("-" * 50)
        print(f"Total Regular Pay: ${total_regular_pay:>13.2f}")
        print(f"Total Overtime Pay: ${total_overtime_pay:>12.2f}")
        print(f"Total Gross Pay: ${total_gross_pay:>15.2f}")
        print(f"Number of Employees: {employee_count:>11}")
        print("-" * 50)

# Run the program
if __name__ == "__main__":
    calculate_payroll()
