import turtle as t
import random

chinky = t.Turtle()
angle = [0, 90, 180, 270]
t.colormode(255)


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


chinky.shape("turtle")
chinky.color(generate_random_color())
chinky.pensize(3)
chinky.speed("fastest")
for i in range(0, 100):
    chinky.pencolor(generate_random_color())
    chinky.setheading(random.choice(angle))
    chinky.forward(20)
t.done()
