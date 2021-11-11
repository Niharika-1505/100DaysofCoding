from turtle import Turtle, done

chinky = Turtle()
for i in range(4):
    for j in range(10):
        chinky.pendown()
        chinky.forward(10)
        chinky.penup()
        chinky.forward(5)
    chinky.right(90)
done()
