import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(550, 550)

def fractal_triangle(size,depth):
    if depth == 0: # base case, draw a triangle
        for i in range(3):
            tina.forward(size)
            tina.left(120)
    else:
        for i in range(3):
            fractal_triangle(size/2,depth-1)
            tina.forward(size)
            tina.left(120)

tina.pen_up()
tina.goto(-200,-200)
tina.pendown()

fractal_triangle(200,4)

turtle.exitonclick()