import time
from turtle import Screen, done
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

user_paddle = Paddle((350, 0))
computer_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkeypress(user_paddle.up, "Up")
screen.onkeypress(user_paddle.down, "Down")
screen.onkeypress(computer_paddle.up, "w")
screen.onkeypress(computer_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle " \ backslash indicates next line in a condition"
    if ball.distance(user_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(computer_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect user paddle misses
    if ball.xcor() > 380:
        ball.reset_ball_position()
        score.computer_score()

    # Detect computer paddle misses
    if ball.xcor() < -380:
        ball.reset_ball_position()
        score.user_score()
screen.exitonclick()
