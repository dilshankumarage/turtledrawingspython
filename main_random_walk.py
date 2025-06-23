from turtle import Turtle, Screen
import random

# Setup screen and color mode
screen = Screen()
screen.colormode(255)  # Must be set before using RGB colors

t = Turtle()
t.shape("turtle")
t.speed("fastest")
t.pensize(15)
# Initial pen thickness



# Random color generator
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Movement directions
directions = [0, 90, 180, 270]

# Random walk loop
for _ in range(200):
    t.color(random_color())
    t.forward(20)
    t.setheading(random.choice(directions))

screen.exitonclick()
