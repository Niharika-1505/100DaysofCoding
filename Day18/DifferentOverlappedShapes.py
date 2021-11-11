import random
from turtle import Turtle, done

chinky = Turtle()
colours = ["DeepPink", "DeepSkyBlue", "DarkOliveGreen3", "DarkOrchid3", "HotPink2", "turquoise1", "VioletRed2",
           "Purple4"]


def draw_shape(num_of_sides):
    angle = abs(360 / num_of_sides)
    for j in range(num_of_sides):
        chinky.forward(100)
        chinky.right(angle)


chinky.shape("arrow")
chinky.pensize(3)
for i in range(3, 11):
    chinky.pencolor(random.choice(colours))
    draw_shape(i)
done()
