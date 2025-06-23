import colorgram

# Extract 10 colors from an image
colors = colorgram.extract('image.jpg', 30)

# Print the RGB values
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

import turtle
import random

# List of RGB colors (example from colorgram extraction)
color_list = [
    (239, 246, 241), (240, 239, 243), (132, 165, 203), (222, 148, 106),
    (33, 42, 60), (201, 135, 148), (236, 212, 89), (141, 184, 162),
    (197, 91, 71), (134, 70, 90), (51, 93, 123), (145, 78, 67),
    (67, 112, 90), (183, 201, 176), (170, 99, 102), (58, 46, 41),
    (32, 60, 55), (114, 127, 156), (179, 188, 211), (105, 126, 154)
]

# Set up turtle
turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

# Start position
tim.setheading(225)
tim.forward(500)
tim.setheading(0)

# Draw 20x20 dots
dots = 20
for row in range(dots):
    for col in range(dots):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(50 * dots)
    tim.setheading(0)

# Exit on click
screen = turtle.Screen()
screen.exitonclick()
