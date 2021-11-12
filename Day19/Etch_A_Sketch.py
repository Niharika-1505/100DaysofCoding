from turtle import Turtle, Screen

chinky = Turtle()
screen = Screen()


def move_forwards():
    chinky.forward(10)


def move_backwards():
    chinky.backward(10)


def turn_left():
    new_heading = chinky.heading() + 10
    chinky.setheading(new_heading)


def turn_right():
    new_heading = chinky.heading() - 10
    chinky.setheading(new_heading)


def clear():
    chinky.clear()
    chinky.penup()
    chinky.home()
    chinky.pendown()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
