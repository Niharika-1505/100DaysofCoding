from turtle import Turtle, done
from math import pi, copysign

chinky = Turtle()
colours = ["DeepPink2", "DarkTurquoise", "chartreuse3", "CornflowerBlue"]


def draw_dotted_circle(radius, dot_size):
    chinky.penup()
    chinky.sety(radius)

    diameter = 2 * radius
    circumference = pi * diameter
    dot_extent = 360 * dot_size / circumference  # diameter to angle

    times_y_crossed = 0
    x_sign = 1

    while times_y_crossed < 2:
        chinky.dot(dot_size)  # draw the dot
        chinky.right(dot_extent)
        chinky.forward(dot_size)

        chinky.right(dot_extent)  # draw the gap
        chinky.forward(dot_size)

        x_sign_new = copysign(1, chinky.xcor())

        if x_sign_new != x_sign:
            times_y_crossed += 1
            x_sign = x_sign_new

    chinky.pendown()


chinky.speed("fastest")
circle_radius = 300
j = 0
while circle_radius != 0:
    chinky.color(colours[j])
    if j <= 3:
        j += 1
    else:
        j = 0
    draw_dotted_circle(circle_radius, 5)
    circle_radius -= 20
done()
