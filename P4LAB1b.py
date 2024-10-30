# Jamarius Berry

# 10/29/2024

# P4LAB1b




import turtle

# Set up the turtle
t = turtle.Turtle()
t.pensize(5)
t.color("red")
t.speed(2)

# Move to starting position
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw J
t.forward(60)  
t.backward(30)  
t.right(90)
t.forward(100)  
t.right(90)
t.forward(40)  

# Move to position for B
t.penup()
t.goto(0, 0)
t.setheading(270)  
t.pendown()

# Draw B
t.forward(100)
t.backward(100)
t.setheading(0)

# Draw top curve of B
t.circle(-25, 180)
t.setheading(0)  
# Draw bottom curve of B
t.circle(-25, 180)

# Hide turtle and keep window open
t.hideturtle()
turtle.done()
