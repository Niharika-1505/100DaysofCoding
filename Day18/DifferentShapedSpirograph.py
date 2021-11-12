import turtle as t
import random

chinky = t.Turtle()
t.colormode(255)


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_a_shape_spirograph(num_of_sides, size_of_gap):
    angle = abs(360 / num_of_sides)
    for i in range(int(360 / size_of_gap)):
        for k in range(num_of_sides):
            chinky.pencolor(generate_random_color())
            chinky.forward(100)
            chinky.right(angle)
        chinky.setheading(chinky.heading() + size_of_gap)


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        chinky.pencolor(generate_random_color())
        chinky.circle(100)
        chinky.setheading(chinky.heading() + size_of_gap)


chinky.pensize(1)
chinky.speed("fastest")
draw_spirograph(2)
for j in range(3, 5):
    draw_a_shape_spirograph(j, 2)
t.done()
