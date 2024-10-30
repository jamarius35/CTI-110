# Jamarius Berry

# 10/29/2024

# P4LAB1a



import turtle
t = turtle.Turtle()
t.speed(2)  
t.pensize(2)  

# Function to draw a square
def draw_square():
    # Starting point for square
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    
    # Draw square using while loop
    sides = 0
    while sides < 4:
        t.forward(100)  
        t.right(90)     
        sides += 1

# Function to draw a triangle
def draw_triangle():
    # Starting point for triangle
    t.penup()
    t.goto(50, 0)
    t.pendown()
    
    # Draw triangle using while loop
    sides = 0
    while sides < 3:
        t.forward(100)  
        t.left(120)     
        sides += 1

# Draw the shapes
draw_square()
draw_triangle()

# User will close window when complete
turtle.exitonclick()
