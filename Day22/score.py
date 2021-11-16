from turtle import Turtle

ALIGN = "center"
FONT_STYLE = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.users_score = 0
        self.computers_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.computers_score, align=ALIGN, font=FONT_STYLE)
        self.goto(100, 200)
        self.write(self.users_score, align=ALIGN, font=FONT_STYLE)

    def user_score(self):
        self.users_score += 1
        self.update_score()

    def computer_score(self):
        self.computers_score += 1
        self.update_score()

