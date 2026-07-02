import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue") # Optional: sets background color

# Create and name our turtle "Tina"
tina = turtle.Turtle()
tina.shape("turtle")
tina.color("green")
tina.pensize(3)

# A regular pentagon has 5 sides and 72-degree exterior angles (360 / 5 = 72)
# We use a loop to repeat the movement and rotation 5 times
for i in range(5):
    tina.forward(100)  # Move forward 100 pixels
    tina.right(72)     # Turn right by 72 degrees

# Keep the drawing window open until the user clicks it
turtle.exitonclick()