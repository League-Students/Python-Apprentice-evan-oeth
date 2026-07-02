import turtle

def draw_polygon(sides):
    """Draws a polygon based on the number of sides."""
    # Calculate the turning angle needed for the given number of sides
    angle = 360 / sides
    
    # Draw the shape
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)

# Set up the turtle window
screen = turtle.Screen()
turtle.speed(2)

# Draw a square (4 sides)
draw_polygon(4)

# Draw a pentagon (5 sides)
draw_polygon(5)

# Draw a hexagon (6 sides)
draw_polygon(6)

# Keep the window open until clicked
turtle.exitonclick()