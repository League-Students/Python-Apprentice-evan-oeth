import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")

tina = turtle.Turtle()
tina.speed(2)
tina.pensize(3)

# List of colors for each side of the pentagon
colors = ["red", "blue", "green", "purple", "orange"]

# Draw a 5-sided shape
for i in range(5):
    tina.pencolor(colors[i])  # Change color before drawing the side
    tina.forward(100)         # Move forward
    tina.left(72)             # Turn left by 72 degrees (360 / 5)

# Keep the drawing window open
turtle.done()