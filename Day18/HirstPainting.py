import turtle as t
import random

t.colormode(255)
chinky = t.Turtle()
chinky.speed("fastest")
chinky.penup()      # comment this and the below line to see the actual direction of flow of dots
chinky.hideturtle()
chinky.setheading(225)
chinky.forward(180)
chinky.setheading(180)
chinky.forward(50)
chinky.setheading(0)


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_hirst_painting(dot_size, space_between_dots, number_of_dots_per_line, total_dots):
    for dot_count in range(1, total_dots + 1):
        chinky.dot(dot_size, generate_random_color())
        chinky.forward(space_between_dots)

        if dot_count % number_of_dots_per_line == 0:
            chinky.setheading(90)
            chinky.forward(space_between_dots)
            chinky.setheading(180)
            chinky.forward(space_between_dots * number_of_dots_per_line)
            chinky.setheading(0)


draw_hirst_painting(10, 10, 38, 1064)
t.done()
