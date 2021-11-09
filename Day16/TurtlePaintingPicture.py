from turtle import *

""" Turtle Graphics : https://docs.python.org/3/library/turtle.html#turtle.begin_fill
    Turtle Colors: https://cs111.wellesley.edu/labs/lab01/colors
"""


color('black', 'DarkMagenta')
shape("turtle")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
