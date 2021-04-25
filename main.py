# import colorgram
#
# colors = colorgram.extract('painting.jpg', 25)
# my_colors = []
#
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_extracted = (red, green, blue)
#     my_colors.append(color_extracted)
#
#
# print(my_colors)

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
the_turtle = Turtle()
the_turtle.penup()
the_turtle.hideturtle()

color_list = [(132, 164, 203), (227, 150, 100), (31, 44, 64), (164, 58, 48), (201, 135, 148), (236, 212, 87), (43, 101, 147), (136, 182, 161), (151, 62, 70), (52, 41, 45), (159, 33, 30), (59, 48, 45), (59, 116, 99), (170, 29, 32), (237, 166, 157), (216, 83, 73), (231, 162, 167), (36, 61, 55), (16, 95, 70), (33, 60, 107), (170, 188, 221), (196, 99, 108), (107, 126, 158), (17, 84, 106), (175, 200, 189), (34, 151, 209)]


def return_to_position():
    """returns the turtle to the beginning of the next line"""
    the_turtle.setheading(90)
    the_turtle.forward(50)
    the_turtle.setheading(180)
    the_turtle.forward(500)
    the_turtle.setheading(0)


the_turtle.setheading(225)
the_turtle.forward(300)
the_turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    the_turtle.dot(20, random.choice(color_list))
    the_turtle.forward(50)

    if dot_count % 10 == 0:
        return_to_position()


screen = Screen()
screen.exitonclick()
