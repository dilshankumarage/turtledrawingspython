from turtle import Turtle, Screen
import random

# Setup screen and color mode
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

# Create turtle
t = Turtle()
t.speed("fastest")
t.width(1)

# Random color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Draw spirograph
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + gap_size)

# Call the function
draw_spirograph(5)

# Exit on click
screen.exitonclick()
