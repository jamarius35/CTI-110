# Jamarius Berry

# 10/9/2024

# P2HW2

# This program will calculate grades for all modules

# Input grades for each module

module_grades = [
    float(input("Enter grade for Module 1: ")),
    float(input("Enter grade for Module 2: ")),
    float(input("Enter grade for Module 3: ")),
    float(input("Enter grade for Module 4: ")),
    float(input("Enter grade for Module 5: ")),
    float(input("Enter grade for Module 6: "))
]

# Calculate grades in all modules

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Display results

print("\n-------------Results--------------")
print(f"{'Lowest Grade:':<15} {lowest_grade:>10.2f}")
print(f"{'Highest Grade:':<15} {highest_grade:>10.2f}")
print(f"{'Sum of Grades:':<15} {sum_of_grades:>10.2f}")
print(f"{'Average Grade:':<15} {average_grade:>10.2f}")


