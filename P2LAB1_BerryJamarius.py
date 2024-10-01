# Jamarius Berry
# 10/1/2024
# P2LAB1
# Using built-in libraires for circle calculations

# Import the math library
import math

# Create a variable to hold pi
pi = math.pi

print(pi)

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate the diameter

diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}")

# Calculate the circumference

circumf = 2 * pi * radius

# Display

print(f"The circumference of the circle is {circumf:.2f}")

# Calculate and display the area

area = math.pi * radius ** 2

print(f"The area of the circle is {area:.3f}")

