from turtle import Turtle

ALIGN = "center"
FONT_STYLE = ("Arial", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def increment_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT_STYLE)

    def crashed_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT_STYLE)
