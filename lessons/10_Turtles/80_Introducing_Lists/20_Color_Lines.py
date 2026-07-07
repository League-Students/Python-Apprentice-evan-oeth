import turtle

# Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0) # Set the size of the window
tina = turtle.Turtle() # Create a turtle named tina
tina.shape('turtle') # Set the shape of the turtle to a turtle
tina.speed(2) # Move at a moderate speed, not too fast.

colors = ['red', 'blue', 'black', 'orange'] # define a list of colors

# 1) Make the first square
for color in colors: # loop through the colors
    tina.pencolor(color) # Set the pen color for the side
    tina.forward(100) # Move forward 100 pixels
    tina.left(90) # Turn left 90 degrees

# 2) Make another square, but put the colors in reverse order
for i in range(-1, -5, -1): # Loop backwards using negative indices (-1, -2, -3, -4)
    tina.pencolor(colors[i]) # Set the pen color to the reverse index
    tina.forward(100) # Move forward 100 pixels
    tina.left(90) # Turn left 90 degrees

turtle.exitonclick() # Close the window when we click on it