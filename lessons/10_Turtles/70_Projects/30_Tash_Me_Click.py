import turtle

# 1. Setup the screen and load the emoji background
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Replace 'emoji.gif' with the exact name of your GIF file
screen.bgpic("emoji.gif") 

# 2. Make the turtle shape a moustache
# Register the moustache image (must also be a .gif) and assign it
screen.addshape("moustache.gif")
t = turtle.Turtle()
t.shape("moustache.gif")

# 3. Move the moustache to the right spot on the emoji
# Lift the pen so it doesn't draw a line when moving
t.penup()

# Move the turtle to the correct (x, y) coordinates
# (0, -50) places it roughly where a mouth/moustache would go on a 600x600 screen
# You can adjust these numbers depending on your emoji's dimensions
t.goto(0, -50)

# Keep the window open until the user clicks
turtle.done()