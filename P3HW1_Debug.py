# Jamarius Berry

# 10/17/2024

# P3HW1

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

lowest = min(grades)
highest = max(grades)
total = sum(grades)
avg = total / len(grades)


# determine letter grade for average


if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F' # TO DO: finish this



# Grade Results

print('\n--------------Results-------------')
print(f"{'Lowest grade:':<15} {lowest:>10.2f}")
print(f"{'Highest grade:':<15} {highest:>10.2f}")
print(f"{'Sum of grades:':<15} {total:>10.2f}")
print(f"{'Average grade:':<15} {avg:>10.2f}")


print('-----------------------------------')
print(f'Your letter grade is: {letter_grade}')





