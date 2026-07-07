import turtle

# Initialize screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# 1) Change the turtle image to 'leaguebot_bot.gif'
screen.register_shape('leaguebot_bolt.gif')
t.shape('leaguebot_bolt.gif')
import turtle

# Initialize screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# 1) Change the turtle image to 'leaguebot_bot.gif'
screen.register_shape('leaguebot_bot.gif')
t.shape('leaguebot_bot.gif')

# 2) Change the turtle size to 10x10
# Note: In the [Python Documentation](https://docs.python.org/3/library/turtle.html), 
# shapesize scales standard shapes; for GIFs, sizing is dictated by the original image file.
t.shapesize(10, 10)

# 3) Change the turtle line color to 'blue'
t.pencolor('blue')
t.pensize(3) # Slightly thicker line for visibility

# 4) Draw a hexagon using a loop and variables
side_length = 100
angle = 60 # 360 degrees / 6 sides = 60 degrees

for i in range(6):
    t.forward(side_length)
    t.left(angle)

# Keep the drawing window open
turtle.done()
# 2) Change the turtle size to 10x10
# Note: In the [Python Documentation](https://docs.python.org/3/library/turtle.html), 
# shapesize scales standard shapes; for GIFs, sizing is dictated by the original image file.
t.shapesize(10, 10)

# 3) Change the turtle line color to 'blue'
t.pencolor('blue')
t.pensize(3) # Slightly thicker line for visibility

# 4) Draw a hexagon using a loop and variables
side_length = 100
angle = 60 # 360 degrees / 6 sides = 60 degrees

for i in range(6):
    t.forward(side_length)
    t.left(angle)

# Keep the drawing window open
turtle.done()