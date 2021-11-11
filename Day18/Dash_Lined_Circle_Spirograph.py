import random
import turtle
from turtle import Turtle, done

chinky = Turtle()
chinky.speed("fastest")
turtle.colormode(255)


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def dotted_circle(radius):
    i = 0
    for j in range(0, int(360 / 10)):
        chinky.pencolor(generate_random_color())
        chinky.circle(radius, i + 5)
        chinky.penup()
        chinky.circle(radius, i + 5)
        chinky.pendown()


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        dotted_circle(100)
        chinky.setheading(chinky.heading() + size_of_gap)


chinky.pensize(1)
chinky.speed("fastest")
draw_spirograph(10)
done()
