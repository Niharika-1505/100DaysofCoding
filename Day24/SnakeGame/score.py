from turtle import Turtle

ALIGN = "center"
FONT_STYLE = ("Arial", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_scores.txt") as read_file:
            self.high_score = int(read_file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def increment_score(self):
        self.score = self.score + 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High_Score: {self.high_score}", align=ALIGN, font=FONT_STYLE)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt", "w") as write_file:
                write_file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
