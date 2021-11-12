from turtle import Turtle, done
from math import pi

chinky = Turtle()
colours = ["DeepPink2", "DarkTurquoise", "chartreuse3", "CornflowerBlue", "DeepPink2",
           "DarkTurquoise", "chartreuse3", "CornflowerBlue", "DeepPink2",
           "DarkTurquoise", "chartreuse3", "CornflowerBlue"]


def draw_dotted_circle_using_circle(radius, dot_size):
    chinky.penup()
    circumference = 2 * pi * radius
    dot_extent = 360 * dot_size * 2 / circumference  # diameter to angle
    extent = 0
    while extent < 360:
        chinky.dot(dot_size)
        chinky.circle(radius, dot_extent)
        extent += dot_extent


radius_of_circles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
j = 0
for i in radius_of_circles:
    chinky.color(colours[j])
    j += 1
    draw_dotted_circle_using_circle(i, 5)
done()
