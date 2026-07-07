import turtle

# Set up the window
turtle.setup(800, 800, 0, 0)
turtle.bgcolor("black")  # Dark background makes the crazy spiral pop!

t = turtle.Turtle()  # Create a turtle named t
t.shape("turtle")
t.speed(0)  # Set to fastest speed so it draws quickly
t.width(2)

# List of vibrant colors for the crazy pattern
colors = ["red", "purple", "blue", "green", "orange", "yellow"]


# 1) Complete make_a_shape() to make the turtle move in some pattern.
def make_a_shape(t):
    """Make a sharp, asymmetric star-like segment with turtle t."""
    t.forward(120)
    t.left(40)
    t.forward(40)
    t.right(130)
    t.forward(50)
    t.left(30)


# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
num_shapes = 120  # Draw 120 shapes to make a dense, overlapping spiral

for i in range(num_shapes):t.pencolor(colors[i % len(colors)])  # Cycle through the list of colors
    make_a_shape(t)
    t.right(360 / num_shapes + 2)  # Adding '+ 2' creates the cascading spiral effect

turtle.exitonclick()