import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3) # Sets drawing speed

# --- Draw the First Circle ---
t.penup()
t.goto(-150, 50) # Moves the turtle without drawing
t.pendown()
t.fillcolor("cyan") # Sets the fill color for the first circle
t.begin_fill()
t.circle(50) # Draws a circle with a radius of 50
t.end_fill()

# --- Draw the Second Circle ---
t.penup()
t.goto(150, -50) # Moves to a different location (no overlap)
t.pendown()
t.fillcolor("orchid") # Sets a different fill color for the second circle
t.begin_fill()
t.circle(70) # Draws a larger circle with a radius of 70
t.end_fill()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()