import random
from turtle import Turtle, Screen

myScreen = Screen()
is_race_on = False
myScreen.setup(width=500, height=400)
user_placed_bet_on = myScreen.textinput(title="Which turtle do you want to bet on? ", prompt="Enter a Color:")
colors = ["violet", "indigo", "blue", "green", "orange", "red"]
y_axis_positions = [-70, -40, -10, 20, 50, 80]  # If colors increase add more y axis positions accordingly
all_turtles_list = []


def creating_turtles():
    for turtles_index in range(0, len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtles_index])
        new_turtle.goto(x=-230, y=y_axis_positions[turtles_index])
        all_turtles_list.append(new_turtle)


creating_turtles()

if user_placed_bet_on:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles_list:
        if turtles.xcor() > 230:  # 250 - half of width of turtle = 230
            is_race_on = False
            winning_turtle_color = turtles.pencolor()
            if user_placed_bet_on.lower() == winning_turtle_color.lower():
                print(f"You've won! The {winning_turtle_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle_color} turtle is the winner!")
        turtles.forward(random.randint(0, 10))
myScreen.exitonclick()
